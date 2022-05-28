import os
import argparse
import hashlib
import difflib
from numpy import full
from pyparsing import line
def check(base,fp):
    all_list=[]
    changed_list=[]
    nf_list=[]
    file=open(base,'r')
    all_list.append(fp)
    for lines in file:
        lines.replace('\n','')
        l=lines.split('\t')
        if(len(l)==1):
            path=l[0].split('/',1)
            if(len(path)>1):
                all_list.append(fp+'/'+path[1].strip())
                if not os.path.isdir(fp+'/'+path[1].strip()) :
                    nf_list.append(path[1])
                    
        else:
            path=l[0].split('/',1)
            all_list.append(fp+'/'+path[1].strip())
            if not os.path.isfile(fp+'/'+path[1].strip()):
                nf_list.append(path[1])
            else:
                ha=file_hex(fp+'/'+path[1])
                if  not ha.strip() == l[1].strip():
                    changed_list.append(path[1])
    lsit=[]
    lsit=new_files(fp,all_list,lsit)
    if(len(changed_list)!=0):
        print("Changed Files")
        for f in changed_list:
            print(f)
    else:
        print("No changed Files")
    if(len(nf_list)!=0):
        print("Files not Found")
        for f in nf_list:
            print(f)
    else:
        print("No removed Files")
    
    if(len(lsit)!=0):
        print("New Files")
        for f in lsit:
            print(f)
    else:
        print("No New Files")

def new_files(path,all_list,list):
    if(os.path.isdir(path)):
        try:
            all_list.index(path)
        except ValueError:
            list.append(path)
        if(os.listdir(path)):
            entry=os.listdir(path)
            for entries in entry:
                return new_files(path+'/'+entries,all_list,list)
    else:
        try:
            all_list.index(path)
        except ValueError:
            list.append(path)

        return list 
    return list
    
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
