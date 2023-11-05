b=input().split()
a=input().split()
b1=[]
b2=""
c=input().split()
for i in range(len(a)):
    if b.count(a[i])==1:
        b1.append(a[i])
for i in range(len(c)):
    if b1.count(c[i])==1:
        b2+=b2+" "+c[i]
if b2=="":
    print("Все три задачи никто не решил")
else:
    print(b2)