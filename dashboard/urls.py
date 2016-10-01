from django.conf.urls import url

from dashboard import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/all$', views.create_all, name='create_all'),
    url(r'^create/vpc$', views.create_vpc, name='create_vpc'),
    url(r'^create/nova$', views.create_nova, name='create_nova'),
    url(r'^create/rds', views.create_rds, name='create_rds'),

    url(r'^terminate/all$', views.terminate_all, name='terminate_all'),
    url(r'^terminate/vpc$', views.terminate_vpc, name='terminate_vpc'),
    url(r'^terminate/nova$', views.terminate_nova, name='terminate_nova'),
    url(r'^terminate/rds', views.terminate_rds, name='terminate_rds'),
    url(r'^terminate/eb-old-env$', views.terminate_elasticbeanstalk_old_env,
        name='terminate_eb_old_env'),

    url(r'^settings/aws-config$', views.setting_aws_config,
        name='setting_aws_config'),
]

