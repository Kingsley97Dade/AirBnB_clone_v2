#!/usr/bin/python3
"""
Fabric script for deploying web_static to web servers.
"""

from fabric import task
from os.path import exists
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<your_username>'
env.key_filename = '<path_to_your_ssh_private_key>'

@task
def do_deploy(c, archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        archive_filename = os.path.basename(archive_path)
        archive_remote_path = "/tmp/" + archive_filename
        c.put(archive_path, archive_remote_path)

        # Extract the archive to /data/web_static/releases/ folder
        release_folder = "/data/web_static/releases/"
        release_folder += archive_filename.split('.')[0] + "/"
        c.run(f"sudo mkdir -p {release_folder}")
        c.run(f"sudo tar -xzf {archive_remote_path} -C {release_folder}")
        c.run(f"sudo rm {archive_remote_path}")

        # Delete the symbolic link /data/web_static/current
        current_link = "/data/web_static/current"
        c.run(f"sudo rm -f {current_link}")

        # Create a new symbolic link pointing to the new version
        c.run(f"sudo ln -s {release_folder} {current_link}")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

