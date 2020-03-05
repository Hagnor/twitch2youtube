import os


def parseOK(path):
    tab_init=[]
    nline=0
    nblien=0
    block=0
    with open (path, 'rt') as infile:  
        for line in infile:
            nline=nline+1
#            print(line)
#            print(nline)
            if  'lien' in line:
                if block!=0:
#                    print("Input file error")
                    exit()
                temp=(line.split('='))[1].rstrip()
                tab_init.append(temp)
                block=nline
                nblien=nblien+1
#                print(block)
            if 'mode' in line:
                if block==0:
#                    print("Input file error")
                    exit()
                temp=(line.split('='))[1].rstrip()
                temp1=nline-(block)
                tab_init.append(temp1-1)            
                tab_init.append(temp)
                block=0
    tab_init.insert(0,nblien)
    return tab_init
            
link="time.txt"
firstparse=parseOK(link)
print(firstparse)
