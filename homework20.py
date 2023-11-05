a=input("имя: ")
b=input("фамилия: ")
c=input("отчество: ")
d=int(input("возраст(год): "))
def pal(x,y,z,o):
    p=2023-o
    r=str(p)+"г.р. зарегистрирован"
    return print(y,x,z,r)
pal(a,b,c,d)