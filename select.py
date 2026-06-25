import os
down="https://en.wikipedia.org/wiki/List_of_x86_instructions"
files="down.html"
finds="Original 8086/8088 instruction set"
select1="Forms"
select2="Operand Stack"
print("\033c\033[47;31m\nfile: "+files)
os.system("curl "+down+" -o "+files)
f1=open(files,"r")
a=f1.read()
f1.close()

b=a.find("<body")
if b<0:
    b=a.find("<BODY")
a=a[b:]
a=a.replace("\n","")
a=a.replace("\r","")
a=a.replace("<tr>","\n")
a=a.replace("<td>"," | ")

bodys=a.split("<")
c=""
for body in bodys:
    t=body.split(">")
    if len(t)>1:
        c=c+t[1]

b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[d:]
finds="Added in specific processors"
b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[:d]
v=c
f1=open(files,"w")
f1.write(v)
f1.close()
