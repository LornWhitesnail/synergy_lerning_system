def pal(x):
    m=-10000000000000
    for i in range(len(x)):
        if x[i]>m:
            m=x[i]
    return m
a=list(map(int, input().split()))
print(pal(a))