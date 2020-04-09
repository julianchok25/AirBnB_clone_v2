#!/usr/bin/python3
""" Creates a .tgz dir [pack from web_static to versions] """
from datetime import datetime
from fabric.operations import *
import os

web01 = "35.229.101.127"
web02 = "34.224.31.196"
env.user = "ubuntu"
env.hosts = [web01, web02]


def do_pack():
    """ pack file into .tgz dir """
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz".format(datetime.now(
        ).strftime("%Y%m%d%H%M%S"))
    except Exception:
        return None


def do_deploy(archive_path):
    """ Deploy files to Server """
    if not os.path.exists(archive_path):
        return False

    path = archive_path.split("/")[1]
    server_dir = "/data/web_static/releases/" + path

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p " + server_dir)
        run("sudo tar -xzf /tmp/" + path + " -C " + server_dir + "/")
        run("sudo rm /tmp/" + path)
        run("sudo mv " + server_dir + "/web_static/* " + server_dir)
        run("sudo rm -rf " + server_dir + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + server_dir + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False

def deploy():
    """ Creates and deploy in my webServer """
    try:
        pack = do_pack()
    except Exception:
        return False

    do_deploy(pack)
