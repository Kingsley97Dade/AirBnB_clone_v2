#!/usr/bin/python3
"""
Fabric script for deleting out-of-date archives.
"""
from fabric.api import run, env, local, cd, lcd


env.hosts = ['34.229.70.201', '52.204.71.189']
env.user = 'Ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """clean generated archives
    Args:
        number: number of archives to exclude
    Note:
        the cleaning deletes less recent ones
    """
    try:
        # context manger for local
        with lcd('versions/'):
            versions = local('ls -t', capture=True).split()
            versions = versions[1:] if number <= 1 else versions[number:]
            for v in versions:
                local(f'rm -rf {v}')

        # context manger for remote
        with cd('/data/web_static/releases'):
            number = 2 if number <= 1 else number + 1
            run(f'ls -t | tail +{number} | xargs rm -rf')

    except Exception:
        pass

