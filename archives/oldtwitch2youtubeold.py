import os
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
                    print("Input file error, lien")
                    exit()
                temp=(line.split('='))[1].rstrip()
                tab_init.append(temp)
                block=nline
                nblien=nblien+1
            if 'mode' in line:
                if block==0:
                    print("Input file error, mode")
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
                    print("Input file error, nom")
                    exit()
                temp=(line.split('='))[1].rstrip()
                tab_init.append(temp)
    tab_init.insert(0,nblien)
    return tab_all

def parsetime(time):
    tabtemp=[]
    tabok=[]
    if '-' in time:
        tabtemp=(time.split('-'))
        for i in range (2):
            if "." in tabtemp[i]:
                tabtemp2=(tabtemp[i].split('.'))
                if len(tabtemp2)==2 or len(tabtemp2)==3:
                    for j in range (len(tabtemp2)):
                        if len(tabtemp2[j])==1:
                            tabtemp2[j]='0'+tabtemp2[j]
                    if len(tabtemp2)==2:
                        tabok.append('00:'+tabtemp2[0]+':'+tabtemp2[1])
                    if len(tabtemp2)==3:
                        tabok.append(tabtemp2[0]+':'+tabtemp2[1]+':'+tabtemp2[2])                        
                else:
                    print("Input file error, plus de 2 .")
                    exit()  
            else:
                a=tabtemp[i]
                if len(a)==1:
                    a='0'+a
                tabok.append('00:'+a+':00')
        retour=tabok[0]+'-'+tabok[1]
        return retour
    else:
        print("Input file error, pas de -")
        exit()
            
link="time.txt"
linkvideo=""
list_fic=[]
pos_nom=[]
firstparse=parseOK(link)
with open (link) as f:
    temp_fic=list(f)
    for element in temp_fic:
        list_fic.append(element.strip()) 
#print(firstparse)
#print(list_fic)
for x in range(len(list_fic)):
    temp=list_fic[x]
    if 'nom' in temp:
        pos_nom.append(x)
#print(pos_nom)
if len(pos_nom)!=len(firstparse):
    print("Input file error")
    exit
for i in range (len(firstparse)):
    posdepart=pos_nom[i]+1
    nombretime=firstparse[i][2]
    for j in range (posdepart, posdepart+nombretime):
        firstparse[i].append(parsetime(list_fic[j]))
print(firstparse)


    
    
