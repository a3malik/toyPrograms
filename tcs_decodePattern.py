'''Decode Pattern 

decode the pattern and then write the program that prints it.

Input: N, where 2>N<=100

N=3
10203010011012
**4050809
****6-7

N=4
1020304017018019020
**50607014015016
****809012013
******10011'''

import sys 
try:
	N=int(input())
except ValueError:
	print("please enter a number")
	sys.exit()
	
if N<2 or N>100:
	print("please enter a number between 2 and 100")
	sys.exit()

x=list(range(N,0,-1))
x2=list(range(1,N+1))


grid=[]
for y in range(N):
	t=''+y*'**'
	grid.append(t)
	
adder=0
for t,p in zip(x,range(len(grid))):
	
	for t2 in range(1,t+1):
		adder+=10
		grid[p]=grid[p]+str(adder)
		

for t,p in zip(x2,range(len(grid)-1,-1,-1)):
	for t2 in range(1,t+1):
		adder+=10
		grid[p]=grid[p]+str(adder)
		
for t in range(len(grid)):
	grid[t]=grid[t][:-1]
		
for t in grid:
	print(t)
		
