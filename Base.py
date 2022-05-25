import os
import argparse
import hashlib

from numpy import full
from pyparsing import line
def check(base,fp):
    changed_list=[]
    nf_list=[]
    file=open(base,'r')
    for lines in file:
        l=lines.split('\t')
        if(len(l)==1):
            path=l[0].split('/',1)
            if not os.path.isdir(fp+'/'+path):
                nf_list.append(path)
        else:
            path=l[0].split('/',1)
            if not os.path.isfile(fp+'/'+path):
                nf_list.append(path)
            else:
                ha=file_hex(fp+'/'+path)
                if ha != l[1]:
                    changed_list.append(path)
    print("Changed Files")
    for f in changed_list:
        print(f)
    print("Files not Found")
    for f in nf_list:
        print(f)

    
    
def baseline_create(path,fd,level,wf):
    if(path==""):
        fullpath=fd
    else:
        fullpath=path+'/'+fd
    if(os.path.isdir(fullpath)):
        file=open("a.txt","a")
        file.write(fullpath+'\n')
        entry=os.listdir(fullpath)
        file.close()
        for entries in entry:
            baseline_create(fullpath,entries,level+1,wf)
    else:
        hex=file_hex(fullpath)
        file=open(wf,"a")
        file.write(f"{fullpath}\t{hex}\n")
        file.close()
def file_hex(fullpath):
    ha=hashlib.md5()
    rfile=open(fullpath,'rb')
    while 1:
        buf=rfile.read(1024)
        if not buf:
            break
        ha.update(buf)
    rfile.close
    return ha.hexdigest()
if __name__=="__main__":
    par=argparse.ArgumentParser()
    par.add_argument('arg1',help="base file/Directory")
    par.add_argument('arg2',help="file/Directory to check")
    args=par.parse_args()
    para1=args.arg1
    para2=args.arg2
    file=open("a.txt",'w')
    file.close()
    baseline_create("",para1,0,"a.txt")
    check("a.txt",para2)
