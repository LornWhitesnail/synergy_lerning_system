n=int(input())
b=[]
for i in range(n):
    a=str(input())
    if b.count(a)==0:
        b.append(a)
print(len(b))