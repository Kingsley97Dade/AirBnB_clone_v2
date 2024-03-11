#!/usr/bin/python3
"""
This module defines a Fabric script that generates a .tgz archive
from the contents of the web_static folder using the do_pack function.
"""

from fabric.api import local, runs_once
from datetime import datetime

@runs_once
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The archive path if the archive has been correctly generated,
             otherwise, None.
    """
    try:
        local('mkdir -p versions')
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = 'web_static_' + time + '.tgz'

        # generate archive in current directory
        local(f'tar -cvzf versions/{archive} web_static')

        return f'versions/{archive}'
    except Exception:
        return None
