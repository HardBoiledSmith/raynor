from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import AWSConfigForm

from .utils import set_aws_config, stream_task


def home(request):
    return render(request, 'home.html')


# ## Create env

def create_all(request):
    data = {
        'action': 'create_all',
    }

    stream_task('create')

    return JsonResponse({'data': data})


def create_vpc(request):
    data = {
        'action': 'create_vpc',
    }

    stream_task('create_vpc')

    return JsonResponse({'data': data})


def create_nova(request):
    data = {
        'action': 'create_nova',
    }

    stream_task('create_nova')

    return JsonResponse({'data': data})


def create_rds(request):
    data = {
        'action': 'create_rds',
    }

    stream_task('create_rds')

    return JsonResponse({'data': data})


# ## Terminate env

def terminate_all(request):
    data = {
        'action': 'terminate_all',
    }

    stream_task('terminate')

    return JsonResponse({'data': data})


def terminate_vpc(request):
    data = {
        'action': 'terminate_vpc',
    }

    stream_task('terminate_vpc')

    return JsonResponse({'data': data})


def terminate_nova(request):
    data = {
        'action': 'terminate_nova',
    }

    stream_task('terminate_nova')

    return JsonResponse({'data': data})


def terminate_rds(request):
    data = {
        'action': 'terminate_rds',
    }

    stream_task('terminate_rds')

    return JsonResponse({'data': data})


def terminate_elasticbeanstalk_old_env(request):
    data = {
        'action': 'terminate_elasticbeanstalk_old_env',
    }

    stream_task('terminate_eb_old_environment')

    return JsonResponse({'data': data})


# ## Settings

def setting_aws_config(request):
    if request.method == 'POST':
        form = AWSConfigForm(request.POST)

        if form.is_valid():
            error = set_aws_config(
                access_key=form.cleaned_data['access_key'],
                secret_key=form.cleaned_data['secret_key'],
                region=form.cleaned_data['region'],
                az1=form.cleaned_data['az1'],
                az2=form.cleaned_data['az2'],
                cname=form.cleaned_data['cname'],
                rds_db=form.cleaned_data['rds_db'],
                rds_user=form.cleaned_data['rds_user'],
                rds_pw=form.cleaned_data['rds_pw']
            )

            if error:
                messages.error(request, 'Error occured.')
            else:
                messages.success(request, 'AWS Configuration is saved successfully.')
            return redirect('/dashboard')
    else:
        form = AWSConfigForm()

    return render(request, 'settings.html', {'form': form})
