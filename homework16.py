a=input()
b=a.split(". ")
a=""
for i in range(len(b)):
    b[i]=b[i][0].capitalize()+b[i][1:]
    if i+1!=len(b):
        b[i]+=". "
    a+=b[i]
b=a.split("! ")
a=""
for i in range(len(b)):
    b[i]=b[i][0].capitalize()+b[i][1:]
    if i+1!=len(b):
        b[i]+="! "    
    a+=b[i]
b=a.split("? ")
a=""
for i in range(len(b)):
    b[i]=b[i][0].capitalize()+b[i][1:]
    if i+1!=len(b):
        b[i]+="? "    
    a+=b[i]
print(a)