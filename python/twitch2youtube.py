import os
#import numpy as np
def parseOK(path):
    tab_init=[]
    tab_all=[]
    nline=0
    nblien=0
    block=0
    with open (path, 'rt') as infile:  
        for line in infile:
            nline=nline+1
            if  'lien' in line:
                if block!=0:
                    print("Input file error")
                    exit()
                temp=(line.split('='))[1].rstrip()
                tab_init.append(temp)
                block=nline
                nblien=nblien+1
            if 'mode' in line:
                if block==0:
                    print("Input file error")
                    exit()
                temp=(line.split('='))[1].rstrip()
                temp1=nline-(block)
                tab_init.append(temp1-2)            
                tab_init.append(temp)
                tab_all.append(tab_init)
                tab_init=[]
                block=0
            if 'nom' in line:
                if block==0:
                    print("Input file error")
                    exit()
                temp=(line.split('='))[1].rstrip()
                tab_init.append(temp)
    tab_init.insert(0,nblien)
#    print(tab_all)
    return tab_all
            
link="time.txt"
list_fic=[]
pos_nom=[]
firstparse=parseOK(link)
with open (link) as f:
    temp_fic=list(f)
    for element in temp_fic:
        list_fic.append(element.strip()) 
print(firstparse)
print(list_fic)
for x in range(len(list_fic)):
    temp=list_fic[x]
    if 'nom' in temp:
        pos_nom.append(x)
print(pos_nom)
if len(pos_nom)!=len(firstparse):
    print("Input file error")
    exit
for i in range (len(firstparse)):
    print(firstparse[i][2])
