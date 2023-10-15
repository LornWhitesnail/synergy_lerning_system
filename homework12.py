a=input()
b=a[:len(a)-2]
c=a[len(a)-1:]
g=c+c
b=b.replace(c, g)
print(b)