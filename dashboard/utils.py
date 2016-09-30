import json
import subprocess

from channels import Group

from .constants import Message


def create_process_of_johanna_command(cmd):
    proc = subprocess.Popen(
        ['python3', '-u', 'run.py', cmd, '--force'],
        cwd=r'../johanna',
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    return proc


def send_log_stream(proc):
    stream = Group('stream')

    for line in iter(proc.stdout.readline, b''):
        line = line.decode('utf-8')

        stream.send({
            "text": json.dumps({
                'code': Message.STREAM_OPENED,
                'log':  line
            })
        })

    stream.send({
        "text": json.dumps({
            'code': Message.STREAM_CLOSED,
            'log':  None
        })
    })

    proc.stdout.close()
    proc.wait()


def stream_task(cmd):
    proc = create_process_of_johanna_command(cmd)
    send_log_stream(proc)


def set_aws_config(access_key=None, secret_key=None, region=None,
                   az1=None, az2=None, cname=None, rds_db=None,
                   rds_user=None, rds_pw=None):
    cmd = ['python3', 'conf.py']
    cmd += ['--accesskey', access_key]
    cmd += ['--secretkey', secret_key]
    cmd += ['--region', region]
    cmd += ['--az1', az1]
    cmd += ['--az2', az2]
    cmd += ['--cname', cname]
    cmd += ['--db', rds_db]
    cmd += ['--user', rds_user]
    cmd += ['--pw', rds_pw]

    output, error = subprocess.Popen(
        cmd,
        cwd=r'../johanna',
        stdout=subprocess.PIPE
    ).communicate()

    print(output)

    return error
