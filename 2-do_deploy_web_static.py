#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers,using the function do_deploy
"""
from fabric.api import *
from fabric.operations import put
from datetime import datetime
import os


env.hosts = ["34.229.66.3", "100.26.234.152"]


def do_deploy(archive_path):
    """Deploys a static archive to my web servers"""

    if not os.path.isfile(archive_path):
        print('archive file does not exist...')
        return False  # Returns False if the file at archive_path doesnt exist
    try:
        archive_tgz = archive_path.split('/')[1]
        archive_no_ext = archive_tgz.split('.')[0]
    except Exception:
        print('failed to get archive name from split...')
        return False

    uploaded = put(archive_path, '/tmp/')
    if uploaded.failed:
        return False
    Res = run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))
    if Res.failed:
        print('failed to create archive directory for relase...')
        return False
    Res = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
               archive_tgz, archive_no_ext))
    if Res.failed:
        print('failed to untar archive...')
        return False
    Res = run('rm /tmp/{}'.format(archive_tgz))
    if Res.failed:
        print('failed to remove archive...')
        return False
    Res = run('mv /data/web_static/releases/{}/web_static/* \
               /data/web_static/releases/{}'
              .format(archive_no_ext, archive_no_ext))
    if Res.failed:
        print('failed to move extraction to proper directory...')
        return False
    Res = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(archive_no_ext))
    if Res.failed:
        print('failed to remove first copy of extraction after move...')
        return False

    # clean up old release and remove it.

    Res = run('rm -rf /data/web_static/current')
    if Res.failed:
        print('failed to clean up old release...')
        return False
    Res = run('ln -s /data/web_static/releases/{} /data/web_static/current'
              .format(archive_no_ext))
    if Res.failed:
        print('failed to create link to new release...')
        return False

    print('New version deployed!\n')

    return False
