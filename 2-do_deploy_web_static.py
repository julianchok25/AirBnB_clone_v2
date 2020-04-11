#!/usr/bin/python3
""" Program that distributes an archive to your web servers,
cusing the function do_deploy """
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['35.243.214.144', '34.233.133.27']


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo """
    date_str = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions/")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(date_str))
        return "versions/web_static_{}.tgz".format(date_str)
    except Exception:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to the web servers """
    if not path.exists(archive_path):
        return False
    # split the path and get the second element in the list
    file_path = archive_path.split("/")[1]
    serv_folder = "/data/web_static/releases/" + file_path

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p " + serv_folder)
        run("sudo tar -xzf /tmp/" + file_path + " -C " + serv_folder + "/")
        run("sudo rm /tmp/" + file_path)
        run("sudo mv " + serv_folder + "/web_static/* " + serv_folder)
        run("sudo rm -rf " + serv_folder + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + serv_folder + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
