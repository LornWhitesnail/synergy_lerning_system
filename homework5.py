a=list(map(str, input().split()))
if (int(a[0])%2==0 and int(a[1])%2==0) or  (int(a[0])%2==1 and int(a[1])%2==1):
    print('NO')
else:
    print('YES')