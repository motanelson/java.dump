import os
import copy
print("\033c\033[47;31m/give me the class file to view ? ")
a=input().strip()
#a="Hello.class"
f1=open(a,"rb")
b=f1.read()
f1.close()

def bins(ui):
    f1=open("/tmp/out.bin","wb")
    f1.write(ui)
    f1.close()
    os.system("rasm2 -a java -D -B -f /tmp/out.bin")
def texts(counts:int,i:chr):
    print(i ,end ="")
    

steps=0
stepsA=True
stepsB=False
ui=bytearray()
count=0
counts=0
for c in b:
    if steps==3:
        print()
        if stepsA:
            
            if c>31 and c<129:
                
                stepsB=False
                steps=4
                
            else:
                stepsB=False
                stepsA=False
                steps=5
        else:
            steps=5
        
                
    if steps==4:
        texts(counts,chr(c))
        if count==0:
            steps=0
        count=count-1
    
    if steps==5:
        
        ui=ui+bytes([c])
        if count==0: 
            steps=0
            bins(ui)
        count=count-1
    if steps==2:
        counts=counts+1
        print("\n"+str(counts),end=" ")
        count=int(c)
        stepsB=True
        print(" "+str(count),end=" ")
        ui=bytearray()
        steps=3
    if steps==1 and c==0:
        steps=2
    if steps==0 and c==1:
        steps=1
    if counts>2:
        pass
        #exit(1)
bins(ui)  