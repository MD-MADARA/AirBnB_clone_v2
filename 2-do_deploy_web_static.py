#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers,using the function do_deploy
"""
from fabric.api import env, put, run
from  os import path

env.hosts = ["34.229.66.3", "100.26.234.152"]


def do_deploy(archive_path):
    """Deploys a static archive to my web servers"""

    if not path.isfile(archive_path):
        return False
    try:
        archive_tgz = archive_path.split('/')[1]
        archive_no_ext = archive_tgz.split('.')[0]
    except Exception:
        return False

    if put(archive_path, '/tmp/').failed is True:
        return False

    if run('mkdir -p /data/web_static/releases/{}/'.format(
        archive_no_ext)).failed is True:
        return False

    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
               archive_tgz, archive_no_ext)).failed is True:
        return False

    if run('rm /tmp/{}'.format(archive_tgz)).failed is True:
        return False

    if run('mv /data/web_static/releases/{}/web_static/* \
               /data/web_static/releases/{}'
              .format(archive_no_ext, archive_no_ext)).failed is True:
        return False

    if run('rm -rf /data/web_static/releases/{}/web_static'
              .format(archive_no_ext)).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -s /data/web_static/releases/{} /data/web_static/current'
              .format(archive_no_ext)).failed is True:
        return False

    print('\nNew version deployed!\n')

    return True
