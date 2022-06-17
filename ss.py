my_ip="192.168.10.12"
my_use="kaizukooni"
import os
import socket
import pwd
import json
from anyio import connect_tcp
import fnmatch
from psycopg2 import connect
import fabric
from cairo import HAS_QUARTZ_SURFACE
host="192.168.10.16"
with open("instances.json") as jfile:
    jdata=json.load(jfile)
    for i in jdata:
        Username=jdata[i]['ssh']['username']
        password=jdata[i]['ssh']['password']
        port=jdata[i]['ssh']['port']
        if(fnmatch.fnmatch(i,"cluster*")):
            print(Username)
            print(password)
            print(port)
Username='hq'
password='qwerty'
port='22'
config = fabric.Config(overrides={'sudo': {'password': 'qwerty'}})
#c = Connection('host', config=config)
#c.sudo('/bin/bash -l -c whoami', user='dev_user')
c=fabric.Connection(f"{Username}@{host}:22",connect_kwargs={'password':f'{password}'},config=config)
c.put('Memory_Image.py','')
c.run('mkdir HQ')
c.run('mv Memory_Image.py HQ/Memory_Image.py')
c.sudo('python HQ/Memory_Image.py -p 12345')
c.run("sshpass -p 'RainGOaway' scp -r -P 22 HQ kaizukooni@192.168.10.12:~/Desktop/ ")
c.close()