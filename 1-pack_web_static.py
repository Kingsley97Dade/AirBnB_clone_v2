#!/usr/bin/python3
"""
This module defines a Fabric script that generates a .tgz archive
from the contents of the web_static folder using the do_pack function.
"""

from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
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

