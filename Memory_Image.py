from genericpath import isdir
import os
import sys
import argparse
par=argparse.ArgumentParser()
par.add_argument('name')
par.add_argument('-p')
par.add_argument('-r')
out=par.parse_args()
pid=out.p
name=out.name
rag=out.r
if(os.path.isdir("Mem_dumps")==0):
    os.mkdir("Mem_dumps")
if(pid):
    i=pid
    if(os.path.isfile(f"/proc/{i}/maps")):
        map_file=f"/proc/{i}/maps"
        mem_file=f"/proc/{i}/mem"
        out_mem=f"{i}.dump"
        out_map=f"{i}.map"
        mapf=open(map_file,'r')
        memf=open(mem_file,'rb')
        outf=open(f'Mem_dumps/{name}.{i}','wb')
        for line in mapf:
            section=line.split(' ')
            if(section[1][0]=='r'):
                address=section[0].split('-')
                st=int(address[0],16)
                end=int(address[1],16)
                memf.seek(st)
                try:
                    outf.write(memf.read(end-st))
                except OSError:
                    print("skipped"+hex(st)+'-'+hex(end)+'\n')
else:
    rag=rag.split('-')
    s=int(rag[0])
    e=int(rag[1])
    for i in range(s,e+1):
        print(i)
        if(os.path.isfile(f"/proc/{i}/maps")):
            map_file=f"/proc/{i}/maps"
            mem_file=f"/proc/{i}/mem"
            out_mem=f"{i}.dump"
            out_map=f"{i}.map"
            mapf=open(map_file,'r')
            memf=open(mem_file,'rb')
            outf=open(f'Mem_dumps/{name}.{i}','wb')
            for line in mapf:
                section=line.split(' ')
                if(section[1][0]=='r'):
                    address=section[0].split('-')
                    st=int(address[0],16)
                    end=int(address[1],16)
                    memf.seek(st)
                    try:
                        outf.write(memf.read(end-st))
                    except OSError:
                        print("skipped"+hex(st)+'-'+hex(end)+'\n')