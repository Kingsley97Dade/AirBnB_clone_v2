#!/usr/bin/python3
"""
Fabric script for deleting out-of-date archives.
"""

from fabric import task
import os
from datetime import datetime

env.hosts = ['34.229.70.201', '52.204.71.189']
env.user = 'Ubuntu'
env.key_filename = '~/.ssh/school'

@task
def do_clean(c, number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): Number of archives to keep. Default is 0.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    try:
        # Delete unnecessary archives in the versions folder
        local_path = "versions"
        archives = sorted(os.listdir(local_path))
        num_to_keep = max(0, number)

        for arch in archives[:-num_to_keep]:
            arch_path = os.path.join(local_path, arch)
            c.local(f"rm -f {arch_path}")

        # Delete unnecessary archives on web servers
        remote_path = "/data/web_static/releases/"
        releases = []
        for host in env.hosts:
            with c.cd(remote_path):
                releases += c.run("ls -1 | grep '^web_static_'").stdout.strip().split('\n')

        releases = sorted(releases, reverse=True)
        for release in releases[:-num_to_keep]:
            release_path = os.path.join(remote_path, release)
            c.run(f"sudo rm -rf {release_path}")

        print("Cleaned up old archives!")
        return True

    except Exception as e:
        print(f"Cleanup failed: {e}")
        return False

