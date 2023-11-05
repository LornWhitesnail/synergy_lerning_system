def pal(x):
    b=1
    for i in range(len(x)//2):
        if x[i]!=x[-i-1]:
            b=0
    if b==1:
        return True
    else:
        return False
a=str(input())
print(pal(a))