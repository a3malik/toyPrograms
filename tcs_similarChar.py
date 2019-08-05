'''
Problem: Similar Char
Problem Description:
Tahir and Mamta are woking in a project in TCS. 
Tahir being a problem solver came up with an interesting problem for his friend Mamta. 
Problem consists of a string of length N and contains only small case alphabets. 
It will be followed by Q queries, in which each query will contain an integer P (1<=P<=N) denoting a position within the string. 
Mamta's task is to find the alphabet present at that location and determine the number of occurrence of same alphabet 
preceding the given location P.
Mamta is busy with her office work. Therefore, she asked you to help her.
Constraints
1 <= N <= 500000
S consisting of small case alphabets
1 <= Q <= 10000
1 <= P <= N
Input Format
First line contains an integer N, denoting the length of string.
Second line contains string S itself consists of small case alphabets only ('a' - 'z').
Third line contains an integer Q denoting number of queries that will be asked.
Next Q lines contains an integer P (1 <= P <= N) for which you need to find the number occurrence of character 
present at the Pth location preceeding P.

Output
For each query, print an integer denoting the answer on single line.
Test Case

Explanation
Example 1
Input
9
abacsddaa
2
9
3
Output
3
1
Explanation
Here Q = 2 
For P=9, character at 9th location is 'a'. Number of occurrences of 'a' before P i.e., 9 is three.
Similarly for P=3, 3rd character is 'a'. Number of occurrences of 'a' before P. i.e., 3 is one.
'''

import sys

print("Enter inputs:")
print("Enter value of N")
try:
	N=int(input())
except ValueError:
	print("Please enter an integer")
	sys.exit()
if N>50000:
	print("Please enter a number smaller than 50000")
	sys.exit()

print("Enter value of S")	
S=input()
if len(S)!=N:
	print("The length of string was",len(S),"please enter string with length=N")
	sys.exit()
for x in S:
	if ord(x)>122 or ord(x)<97:
		print("please enter all lower-case letters as the value of S")
		sys.exit()

print("Enter value of Q")
try:
	Q=int(input())
except ValueError:
	print("Please enter a number")
	sys.exit()
if Q>1000:
	print("Please enter a value less than 1000")
	sys.exit()

print("You entered following inputs")
print("N=",N)
print("S=",S)
print("Q=",Q)

print("Enter queries, i.e. the values of P")
counter=0
collect=[]
while(counter<Q):
	try:
		query=int(input())
		if query>N:
			print("P has exceeded the value of N, please try again")
			continue
		counter+=1
		collect.append(query)
	except ValueError:
		print("Please enter a number")
		
print("You entered following queries")
print(collect)

def char_counter(x):
	char=S[x-1]
	substr=S[:x-1]
	return len(substr.split(char))-1
	
output=[]
for x in collect:
	output.append(char_counter(x))
	
print("The answer is")
for x in output:
	print(x)

	
