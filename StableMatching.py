from Matching import Match
import sys
import os 

def pathing_creator(name:str)->str:
    path=''
    if getattr(sys,'frozen',False):
        path=os.path.dirname(os.path.realpath(sys.executable))  
    elif __file__:
        path=os.path.dirname(__file__)
    return os.path.join(path,'MatchingInput',name)

file=pathing_creator('input.txt')
applicantdata=[]
positiondata=[]
switch=False
with open(file,"r") as rawdata:
    data=rawdata.read()
    compiled=data.split('\n')
    rawdata.close()
for line in compiled:
    if line=='':
        switch=True
    elif switch:
        applicantdata.append([x.strip() for x in line.split(",")])
    else:
        positiondata.append([x.strip() for x in line.split(",")])

matching=Match(applicantdata,positiondata)
matching.stableMatch()
print(matching)




    

