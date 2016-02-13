#Write a function that does the following:
#Input: An array A of length N. N is an even number and N >= 2.
#Output: A reordered array B. The first half of B contains elements of A with even indices. The second half of B contains  elements of A with odd indices. 
#Convention: the first index of an array is 0 (and thus it is an even number).

#Function using for-loop 
def reArrange1(a):
	b = []
	c = []
	for i in range (len(a)):
		if i % 2 == 0:
			b.append(a[i])
		else:
			c.append(a[i])
	result = b + c
	return result 

#Recursive function 
def swap(array, position1, position2):
	temp = array[position1]
	array[position1] = array[position2]
	array[position2] = temp

def reArrange(part, first, last):
	if first >= last: 
		return
	for i in range (first + 2, last+1, 2):
		swap(part, i, i-1)
	first+=1
	last-=1
	reArrange(part,first,last)
	
def main(): 
	a = [1,5,18,34,3,9]
	print reArrange1(a)
	reArrange(a,0,len(a)-1)
	print a 

main()