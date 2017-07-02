#!/bin/python3

import sys
t=int(input())
for i in range(0,t):

	m,n=input().strip().split(' ')
	m,n=[int(m),int(n)]
	if((m%2==0 or n%2==0)and(m!=1 and n!=1)):
		print("Yes\n")
	elif((m==1 and n==2) or (m==2 and n==1)):
		print("Yes\n")
	else:
		print("No\n")
	#s=input().strip()