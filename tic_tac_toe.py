from random import randint
print("Map:")
def you(a1,a2,a3,a4,a5,a6,a7,a8,a9):
	print(a1,"|",a2,"|",a3) 
	print("----------")
	print(a4,"|",a5,"|",a6)
	print("----------")
	print(a7,"|",a8,"|",a9)
you(0,1,2,3,4,5,6,7,8)
a=["*","*","*","*","*","*","*","*","*"]
print("You play: X")
b=randint(0,1)
you(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],)
print("")
if b==1:
	print("YOU")
	f=0
	while f!=1:
		w=int(input())
		if w>=0 and w<=9:
			f=1
		else:
			print("False")
	a[w]="X"
	you(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],)
	print("")
win=0
b=1
while "*" in a !=0 and win ==0:
	if b==1:
		f=0
		while f!=1:
			c=randint(0,8)
			if a[c]=="*":
				f=1
		a[c]="O"
		b=0
		you(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],)
		print("")
	else:
		f=0
		while f!=1:
			w=int(input())
			if a[w]=="*":
				f=1
		a[w]="X"
		you(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],)
		print("")
		b=1
	
	if a[0]=="X" and a[4]=="X" and a[8]=="X":
		win=1
		print("You win")
	elif a[1]=="X" and a[4]=="X" and a[7]=="X":
		win=1
		print("You win")
	elif a[2]=="X" and a[4]=="X" and a[6]=="X":
		win=1
		print("You win")
	elif a[3]=="X" and a[4]=="X" and a[5]=="X":
		win=1
		print("You win")
	elif a[0]=="X" and a[3]=="X" and a[6]=="X":
		win=1
		print("You win")
	elif a[1]=="X" and a[4]=="X" and a[7]=="X":
		win=1
		print("You win")
	elif a[2]=="X" and a[5]=="X" and a[8]=="X":
		win=1
		print("You win")
	elif a[0]=="O" and a[4]=="O" and a[8]=="O":
		win=1
		print("You lose")
	elif a[1]=="O" and a[4]=="O" and a[7]=="O":
		win=1
		print("You lose")
	elif a[2]=="O" and a[4]=="O" and a[6]=="O":
		win=1
		print("You lose")
	elif a[3]=="O" and a[4]=="O" and a[5]=="O":
		win=1
		print("You lose")
	elif a[0]=="O" and a[3]=="O" and a[6]=="O":
		win=1
		print("You lose")
	elif a[1]=="O" and a[4]=="O" and a[7]=="O":
		win=1
		print("You lose")
	elif a[2]=="O" and a[5]=="O" and a[8]=="O":
		win=1
		print("You lose")
if win==0:
	print("draw")