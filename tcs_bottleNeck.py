'''Problem Description:
There are N bottles. ith bottle has A[i] radius. 
Once a bottle is enclosed inside another bottle, it ceases to be visible. 
Minimize the number of visible bottles.
You can put ith bottle into jth bottle if following condition is fulfilled:
1) ith bottle itself is not enclosed in another bottle.
2) jth bottle does not enclose any other bottle.
3) Radius of bottle i is smaller than bottle j (i.e. A[i] < A[j]).
Constraints
1 <= N <= 100000.
1 <= A[i] <= 10^18.

Input Format:
First line contains a single integer N denoting the number of bottles.
Second line contains N space separated integers, ith integer denoting the radius of Ith bottle.
(1 <= i <= N).

Output:
Minimum number of visible bottles.

Test Case/Explanation:
Example 1
Input
8
1 1 2 3 4 5 5 4
Output
2
Explanation
1st bottle can be kept in 3 rd one 1-->2 , which makes following bottles visible [1,2,3,4,5,5,4]
similarly after following operations, the following will be the corresponding visible bottles
Operation ? Visible Bottles
2 ? 3 [1,3,4,5,5,4]
3 ? 4 [1,4,5,5,4]
4 ? 5 [1,5,5,4]
1 ? 4 [5,5,4]
4 ? 5 [5,5]
finally there are 2 bottles which are visible. Hence, the answer is 2'''


'''An other way of looking at this problem is like this. We need to find all possible ascending 
sequences without repeating a number. So let's solve this.'''

print("Enter number of bottles")
n=int(input())
print("Enter radius of bottles separated by space")
arr=input().split(' ')
l=[]
for x in arr:
	l.append(int(x))
s=set(l)
l2=list(s)
d={}
for x in s:
	d[x]=l.count(x)

collect=[]
def splitSequences():
	seq=[]
	for n in l2:
		if d[n]==0:
			pass
		else:
			seq.append(n)
			d[n]=d[n]-1
	seq.sort()
	return seq
	
while sum(d.values())>0:
	collect.append(splitSequences())

print(len(collect))

	

	

