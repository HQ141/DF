import sys
import argparse
par=argparse.ArgumentParser()
par.add_argument('pid')
out=par.parse_args()
pid=out.pid
map_file=f"/proc/{pid}/maps"
mem_file=f"/proc/{pid}/mem"
out_mem=f"{pid}.dump"
out_map=f"{pid}.map"
mapf=open(map_file,'r')
memf=open(mem_file,'rb')
outf=open('ww','wb')
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
