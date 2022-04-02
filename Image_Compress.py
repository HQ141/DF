import hashlib
from os import _EnvironCodeFunc
import tarfile
import time
import argparse
par=argparse.ArgumentParser()
par.add_argument('file')
par.add_argument('-b')
out=par.parse_args()
src=open(out.file,'rb')
tm =str(time.time())
by=b'x00'
evidence=open("Image",'wb')
hash_al=hashlib.md5()
while by:
    by=src.read(out.b)
    evidence.write(by)
    hash_al.update(by)
hash_al.update(tm.encode())
print(hash_al.hexdigest())
src.close()
evidence.close()
compres=tarfile.open('Image.tar','w:xz')
compres.add('Image')
compres.close()