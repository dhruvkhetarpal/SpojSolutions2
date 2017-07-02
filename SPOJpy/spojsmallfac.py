import sys
def fac(a):
	fact=1
	for i in range (1,a+1):
		fact=fact*i
	return fact
t=int(input())
for i in range(0,t):
	n=int(input())
	print(fac(n))