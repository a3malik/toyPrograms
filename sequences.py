'''This program picks sequences of numbers out of an ordered list'''
'''Example:
	input=[1,4,7,9,10,11,12,13,14,20,21,22,25,26,27,31]
	output=[[1],[4],[7],[9,10,11,12,13,14],[20,21,22],[25,26,27],]31]]
'''
import re
p=re.compile('-\*[-*]*')
x=[1,4,7,9,10,11,12,13,14,20,21,22,25,26,27,31]
def sequences(inlist):
	collect=[]
	second=list(range(min(inlist),max(inlist)+1))
	for i in range(len(second)):
		if inlist[i]!=second[i]:
			inlist.insert(i,'*')
	for i in range(len(inlist)):
		inlist[i]=str(inlist[i])
	inlist='-'.join(inlist)
	for x in p.split(inlist):
		collect.append(x.split('-'))
	return collect
#print(sequences(x))

'''The above definition of sequences produces a list where our numbers become strings
here is an alternate implementation of the same function, which retains the list 
items' type as number.'''

from collections import deque
def sequences(inlist):
	dq=deque(inlist)
	collect=[]
	temp=[]
	idx=0
	temp.append(inlist[idx])
	dq.popleft()
#	dq.append('dummy')
	while len(dq)>0:
		nextitem=dq.popleft()
		if inlist[idx]+1==nextitem:
			temp.append(nextitem)
		else:
			collect.append(temp)
			temp=[]
			temp.append(nextitem)
		idx+=1
	collect.append(temp)
	'''if collect[-1][-1]+1==inlist[idx]:
		collect[-1].append(inlist[idx])
	else:
		temp.clear();temp=[]
		temp.append(inlist[idx])
		collect.append(temp)'''
	return collect
print(sequences(x))
	
