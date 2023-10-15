a=input().replace("(", "!@!")
a=a.replace(")", "!@!")
a=a.split("!@!")
b=a[1::2]
print(b)