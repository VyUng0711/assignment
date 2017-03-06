from bitarray import bitarray
import uuid
import math
import random, string
import matplotlib.pyplot as plt
def hash1(string):
	ans = 0 
	for chr in string: 
		ans = ans * 128 + ord(chr) 
	return ans
def hash2(string):
    _hash = 5381
    for i in xrange(0, len(string)):
       _hash = ((_hash << 5) + _hash) + ord(string[i])
    return _hash


class BloomFilter:
	def __init__(self, size):
		self.size = size
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self,string):
		result1 = hash1(string)%self.size
		result2 = hash2(string)%self.size
		self.bit_array[result1]=1
		self.bit_array[result2]=1

	def lookup(self, string):
		b1 = hash1(string)%self.size
		b2 = hash2(string)%self.size
		if self.bit_array[b1] == 1 and self.bit_array[b2] == 1:
			return True
		else:
			return False

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def comparing():
	bf = BloomFilter(1000)
	print bf.__dict__
	num_items = [i for i in range(10000)]
	real = []
	em_rates = []
	theo_rates = []
	test_set = []
	for k in range(1001):
		test_item = randomword(random.randint(0,10))
		test_set.append(test_item)
	for i in num_items:
		word = randomword(random.randint(0,10))
		real.append(word)
		bf.add(word)
		found_false = 0
		test = 0
		for j in test_set:
			if bf.lookup(j):
				test+=1
				if j not in real:
					found_false+=1
		if test == 0:
			em_rate = 0
		else:
			em_rate = found_false/float(test)
		em_rates.append(em_rate)
		theo_rate = (1-(math.e)**((-2*i)/float(100)))**2
		theo_rates.append(theo_rate)
		#print bf.__dict__
	plt.plot(num_items,em_rates,label = "Empirical" )
	plt.xlabel('Number of items stored')
	plt.ylabel('False positive rate')
	print em_rates
	#print real
	plt.plot(num_items,theo_rates,label = "Theory" )
	plt.legend()
	plt.show()
comparing()


def implementation():
	bf1 = BloomFilter(10)
	print bf1.__dict__
	bf1.add('abc')
	bf1.add('cba')
	bf1.lookup('ade')
	h1 = hash1('abcdlakjfklsdjfalkjfkl')
	print h1
	h2 = hash2('ade')
	print h2

#implementation()






