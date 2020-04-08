#!/usr/bin/python3
""" Creates a .tgz dir [pack from web_static to versions] """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ pack file into .tgz dir """
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz web_static/".format(datetime.now(
        ).strftime("%Y%m%d%H%M%S"))
    except Exception:
              return None
