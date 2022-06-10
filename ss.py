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
c=fabric.Connection(f"{Username}@{host}:22",connect_kwargs={'password':f'{password}'})
c.run("sshpass -p 'RainGOaway' scp -P 22 kaizukooni@192.168.10.12:~/Desktop/a ~/Desktop")