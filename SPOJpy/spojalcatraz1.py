import sys
t=int(input())
for i in range(0,t):
	e=0
	s=input()
	for j in range(0,len(s)):
		e+=int(s[j])
	print(e)