# -*- coding: utf-8 -*-
###The Not-So-Basics


#Sorting
x = [4,1,2,3]	# is [1,2,3,4], x is unchanged
y = sorted(x)	# now x is [1,2,3,4]
x.sort()

# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,-3],key=abs,reverse=True) 

# sort the words and counts from highest count to lowest
word_counts = {}
wc = sorted(word_counts.items(),
		key=lambda(word,count): count,
		reverse=True)
print x



#List Comprehensions

even_numbers 	= [x for x in range(5) if x % 2 == 0] #[0,2,4]
squares 	= [x * x for x in range(5)] # [0,1,4,9,16]
even_squares	= [x * x for x in even_numbers] #[0,4,16]

print even_squares

square_dict = {x : x * x for x in range(5) } # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set  = {x * x for x in [1,-1]} # { 1 }
print square_dict

zeroes = [0 for _ in even_numbers] # has the same length as even_numbers
print zeroes

pairs = [(x,y)
	 for x in range(10)
	 for y in range(10)] # 100 pairs (0,0) (0,1) ... (9,8), (9,9)


increasing_pair = [(x,y)			# only pairs with x < y,
		   for x in range(10)		# range(lo, hi) equals
		   for y in range(x+1,10)] 	# [lo, lo + 1, ..., hi - 1] 
print increasing_pair


#Generators and Iterators
def lazy_range(n):
	"""a lazy version of range"""
	i = 0
	while(i<n):
		yield i
		i += 1

#for i in lazy_range(10):
#	do_something_with(i)


def natural_numbers():
	""" Returns 1, 2, 3 ... """
	i = 0
	while(True):
		yield i
		i += 1


lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print lazy_evens_below_20



#Randomness
import random


four_uniform_randoms = [random.random() for _ in range(4)]

#print four_uniform_randoms
#random.seed(10)
#print random.random()
#random.seed(10)
#print random.random()

print random.randrange(10)
print random.randrange(3,6)

up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

my_best_friend = random.choice(["Alice","Bob","Charlie"])
print my_best_friend 


lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers,6)
print winning_numbers

four_with_replacement = [random.choice(range(10)) for __ in range(4)]
#four_with_replacement = [random.randrange(10) for __ in range(4)]
print four_with_replacement



#Regular Expressions
import re
print all([
	not re.match("a","cat"), #* 'cat' doesn't start with 'a'
	re.search("a","cat"),
	not re.search("c","dog"),
	3 == len(re.split("[ab]","carbs")),
	"R-D-" == re.sub("[0-9]","-","R2D2")	
]); #PRINTS true



#Object-Oriented Programming


#Pascal CasesNames
class Set:
	
	def __init__(self,values=None):
		"""This is the constructor
		s1 = Set() = #empty set
		s2 = Set([1,2,2,3]) = #With initial values"""
		self.dict = {} #Cada instância tem seu próprio dicionário
		
		if values is not None:
			for value in values:
				self.add(value)
		
	def add(self,value):
		self.dict[value] = True
	
	def contains(self,value):
		return value in self.dict
	
	def remove(self,value):
		del self.dict[value]



s1 = Set([1,2,3])
s1.add(4)
print s1.contains(4)
s1.remove(3)
print s1.contains(3)



#Functional Tools

def exp(base,power):
	return base ** power

def two_to_the(power):
	return exp(2,power)
	

from functools import partial
two_to_the = partial(exp,2)
print two_to_the(5)

square_of = partial(exp,power=2)
print square_of(3)








