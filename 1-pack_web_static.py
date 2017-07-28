#!/usr/bin/python3
'''Fabric script that generates a .tgz(zipped, tar) archive
   comprised of web static content '''

from fabric.api import *
from datetime import datetime
from time import strftime


def do_pack():
    ''' Method archives files and returns path of archive '''
    time_created = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/web_static_20170314233357.tgz web_static')

    if archive is not None:
        return ('versions/web_static.{}'.format(time_created))
    else:
        return None
