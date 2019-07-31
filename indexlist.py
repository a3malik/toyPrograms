'''The indexlist function takes a source and a serach string as arguments 
and returns a list containing the starting positions of all matches of search 
in the source'''
'''
Example:
	source='This has three spaces'
	search=' '
	indexlist(source,search)
	[4,8,14]
'''

def indexlist(src,srch):
	collect=[]
	if src.find(srch)==-1:
			return None 
	else:
		x=0
		while x!=-1:
			x=src.find(srch)
			collect.append(x)
			src=src[x+len(srch):]
		if collect[len(collect)-1]==-1:
			collect.pop()
	return collect
