#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo,using the function do_pack.

from os.path import exists
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    time = datetime.now().strftime("%Y%-m%-d%-H%-M%-S")
    file_name = f"versions/web_static_{time}.tgz"

    if not exists("versions"):
        local("mkdir versions")
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
