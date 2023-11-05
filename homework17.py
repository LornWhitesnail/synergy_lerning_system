a=str(input())
b=1
for i in range(len(a)//2):
    if a[i]!=a[-i-1]:
        b=0
if b==1:
    print("YES")
else:
    print("NO")