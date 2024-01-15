#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import env, put, run
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
env.hosts = ['34.229.66.3', '100.26.234.152']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        dest_path = f"/data/web_static/releases/{no_ext}"
        if (
            put(archive_path, '/tmp/').failed or
            run(f'mkdir -p {dest_path}/').failed or
            run(f'tar -xzf /tmp/{file_name} -C {dest_path}/').failed or
            run(f'rm /tmp/{file_name}').failed or
            run(f'mv {dest_path}/web_static/* {dest_path}/').failed or
            run(f'rm -rf {dest_path}/web_static').failed or
            run(f'rm -rf /data/web_static/current').failed or
            run(f'ln -s {dest_path}/ /data/web_static/current').failed
        ):
            return False
    except Exception:
        return False
    print("New version deployed!")
    return True
