from Matching import Match
import sys
import os 

def pathing_creator(name:str)->str:  #pathing in VScode is odd, so this is added to fix it. Shouldn't cause any issues with other IDE's
    path=''
    if getattr(sys,'frozen',False):
        path=os.path.dirname(os.path.realpath(sys.executable))  
    elif __file__:
        path=os.path.dirname(__file__)
    return os.path.join(path,'MatchingInput',name)  

file=pathing_creator('input_4.txt')
applicantdata=[]
positiondata=[]
switch=False
with open(file,"r") as rawdata:
    data=rawdata.read()
    compiled=data.split('\n')
    rawdata.close()
for lines in compiled:
    if lines=='':
        switch=True
    elif switch:
        applicantdata.append([line.strip() for line in lines.split(",")])
    else:
        positiondata.append([line.strip() for line in lines.split(",")])

matching=Match(applicantdata,positiondata)
matching.stableMatch()
print(matching)




    

