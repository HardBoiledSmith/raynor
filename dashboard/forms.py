from django import forms
from django.forms import ValidationError
from django.utils.translation import ugettext as _


class AWSConfigForm(forms.Form):
    AWS_REGIONS = (
        'us-east-1',
        'us-west-1',
        'us-west-2',
        'eu-west-1',
        'eu-central-1',
        'ap-southeast-1',
        'ap-southeast-2',
        'ap-northeast-1',
        'ap-northeast-2',
        'ap-south-1',
        'sa-east-1',
    )

    AWS_RDS_ENGINES = (
        'mysql',
        'oracle-se1',
        'oracle-se2',
        'oracle-se',
        'oracle-ee',
        'sqlserver-ee',
        'sqlserver-se',
        'sqlserver-ex',
        'sqlserver-web',
        'postgre',
        'aurora',
    )

    access_key = forms.CharField(label='Access Key', required=True)
    secret_key = forms.CharField(label='Secret Key', widget=forms.PasswordInput,
                                 required=True)
    region = forms.CharField(label='Region', required=True)
    az1 = forms.CharField(label='Availability Zone 1', required=True)
    az2 = forms.CharField(label='Availability Zone 2', required=True)
    cname = forms.CharField(label='CNAME', required=True)
    rds_db = forms.CharField(label='RDS DB Engine', required=True)
    rds_user = forms.CharField(label='RDS User', required=True)
    rds_pw = forms.CharField(label='RDS Password', widget=forms.PasswordInput,
                             required=True)

    def clean_rds_db(self):
        rds_db = self.cleaned_data.get('rds_db')

        if rds_db not in self.AWS_RDS_ENGINES:
            raise ValidationError(
                _('Invalid db %(value)s'),
                params={'value': rds_db},
            )

        return rds_db

    def clean(self):
        cleaned_data = super().clean()

        region = cleaned_data.get('region')
        az1 = cleaned_data.get('az1')
        az2 = cleaned_data.get('az2')

        if region not in self.AWS_REGIONS:
            raise ValidationError(
                _('Invalid region %(value)s'),
                params={'value': region},
            )

        if region not in az1:
            raise ValidationError(
                _('Invalid AZ1 %(value)s'),
                params={'value': az1}
            )

        if region not in az2:
            raise ValidationError(
                _('Invalid AZ2 %(value)s'),
                params={'value': az2}
            )

        return cleaned_data
