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
print(sequences(x))
