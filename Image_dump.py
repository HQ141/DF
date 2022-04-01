import tarfile
import requests
import os
import requests
import hashlib
import tqdm
path ="/dev/sdd"
has=hashlib.sha256()
sc=open(path,"rb")
dest=open("/home/kaizukooni/Desktop/image.iso","wb")
print("Wainting for extractoion to complete\n")
while 1:
    block=sc.read(1024)
    if not block:
        break
    dest.write(block)
    has.update(block)
sc.close()
dest.close()
print("Hash of ISO image " + has.hexdigest())
h1=has.hexdigest()
hase=hashlib.sha256()
tar=tarfile.open("evidence.tar","w:gz")
tar.add("image.iso")
tar.close()
comp=open("evidence.tar","rb")
print("Waiting for hashing\n")
block =0
while 1:
    block=comp.read(1024)
    if not block :
        break
    hase.update(block)
print("Hash of Compressed file " + hase.hexdigest())
h2=hase.hexdigest()
url = 'https://hookb.in/r10D1dxPMXiqk2XXBdBL'

data={"Hash of Image": h1,"Hash of Archive" : hase}
r = requests.post(url,data)
