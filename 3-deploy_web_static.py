#!/usr/bin/python3
"""
Fabric script for creating and distributing an archive to web servers.
"""

from fabric import task
from datetime import datetime
import os

env.hosts = ['34.229.70.201', '52.204.71.189']
env.user = 'ubuntu'


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated,
             otherwise, None.
    """
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Run tar command to create the archive
    result = c.local(f"tar -cvzf {archive_path} web_static")

    if result.succeeded:
        print(f"File packed: {archive_path}")
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
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

def deploy():
    """
    Creates and distributes an archive to web servers.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    archive_path = do_pack(c)

    if not archive_path:
        return False

    return do_deploy(c, archive_path)

