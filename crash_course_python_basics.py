# -*- coding: utf-8 -*-
from __future__ import division



#Zen of Python
import this

#Whitespace Formatting
for i in [1,2,3,4,5,6]:
	print i
	for j in [1,2,3,4,5]:
		print j
		print i + j
	print i
print "done looping"


long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

easier_to_read_list_of_lists = [ [1, 2, 3],
[4, 5, 6],
[7, 8, 9] ]

two_plus_three = 2 + \
		 3
#modulos
import re as regex
my_regex = regex.compile("[0-9]+",regex.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

print (5/2)

#Functions
def double(x):
	"""this function multiply the variable x by two
	pula mais de uma linha com 3 aspas"""
	return x * 2

print (double(2.5))


def apply_to_one(f):
	"""calls the functions f with 1 as its argument"""
	return f(1)


x = apply_to_one(double)
print x


y = apply_to_one(lambda x: x + 4)
print y


#another_double = lambda x: 2 * x
def another_double(x): return 2 * x


print another_double(10)


def my_print(message="my default message"):
	print message

my_print("hello")
my_print()


def subtract(a=0,b=0):
	return a - b

print subtract(10,5)
print subtract(0,5)
print subtract(b=5)


#strings
single_quoted_string = 'data science'
double_quoted_string = "data science"
tab_string = '\t' #representa o caracter tab
print len(tab_string)

not_tab_string = r'\t'	#representa o caracter '\' e o 't'
print len(not_tab_string)


multi_line_string = '''This is the first line.
and this is the second line '''
print multi_line_string


#Exceptions
try:
	print 0/0
except ZeroDivisionError:
	print "Nao pode dividir por zero"

#Lists
integer_list = [1,2,3]
heterogeneous_list = ["string",0.1,True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
print list_of_lists

print len(integer_list)

x = range(10)
print x
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1


first_three = x[:3]
tree_to_end = x[3:]
one_to_four = x[1:5]
last_tree = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]
print copy_of_x

print (1 in [1,2,3])
print (0 in [1,2,3])

x = [1,2,3]
x.extend([4,5,6])
print x

x = [1,2,3]
y = x + [4,5,6]


x = [1,2,3]
x.append(0)
y = x[-1]
z = len(x)

x,y = [1,2]

_,y = [1,2]


#Tuples
my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3

print my_list

try:
	my_tuple[1] = 3
except TypeError:
	print "cannot modify a tuple"


def sum_and_product(x,y):
	return (x+y),(x*y)

sp = sum_and_product(2,3)
print sp
s,p = sum_and_product(5,10)
print s,p


x,y = 1,2
x,y = y,x # Pythonic way to swap variables; now x is 2, y is 1


#Dictionaries
empty_dict = {} 		# Pythonic
empty_dict2 = dict() 		# less Pythonic
grades = { "Joel":80,"Tim":95 } # dictionary literal


joels_grade = grades["Joel"]	#80

try:
	kates_grades = grades["kate"]
except KeyError:
	print "no grade for Kate!"


joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

joels_grade = grades.get("Joel",0) # equals 80
kates_grade = grades.get("Kate",0) # equals 0 
no_ones_grade = grades.get("No one") # default default is None
print no_ones_grade

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print grades

tweet = {
	"user": "joelgrus",
	"text": "Data science is awesome",
	"retweet_count" : 100,
	"hashtags" : ["#data","#science","#datascience","#awesome","#yolo"]
}


tweet_keys = tweet.keys() #list of keys
tweet_values = tweet.values() #list of values
tweet_items = tweet.items() #list of (key, value) tuples

print tweet_items

"user" in tweet_keys
"user" in tweet
"joelgrus" in tweet_values


#defaultdict

document = []

word_counts = {}
for word in document:
	if word in word_counts:
		word_counts[word] += 1
	else:
		word_counts[word] = 1


word_counts = {}
for word in document: 
	try: 
		word_counts[word] += 1
	except KeyError:
		word_counts[word] = 1



word_counts = {}
for word in document:
	previous_count = word_counts.get(word,0)
	word_counts[word] = previous_count + 1

	

from collections import defaultdict

word_counts = defaultdict(int) # int() produces 0
for word in document:
	word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1) # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle" # { "Joel" : { "City" : Seattle"}}

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1 # now dd_pair contains {2: [0,1]}


#Counter
from collections import Counter
c = Counter([0,1,2,0]) # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }

word_counts = Counter(document)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
	print word, count



#Sets
s = set()
s.add(1) 	# s is now { 1 }
s.add(2) 	# s is now { 1, 2 }
s.add(2) 	# s is still { 1, 2 }
x = len(s) 	# equals 2
y = 2 in s 	# equals True
z = 3 in s 	# equals False
print y,z

hundreds_of_other_words = ["b","c","d","...fingequetem95","zz34","zz35"]
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet","you"]
"zip" in stopwords_list 		# False, but have to check every element
stopwords_set = set(stopwords_list)
"zip" in stopwords_set 			#very fast to check

item_list = [1,2,3,1,2,3] 
num_items = len(item_list) 		#6
item_set = set(item_list) 		# {1, 2, 3}
num_distinct_items = len(item_set) 	#3
distinct_item_list = list(item_set) 	# [1, 2, 3]
print distinct_item_list



#Control Flows
if 1 > 2:
	message = "if 1 only..."
elif 1 > 3:
	message = "elif.."
else:
	message = "else... "

parity = "even" if x % 2 == 0 else "odd"

x = 0
while x < 10:
	print x, "is less than 10"
	x += 1

for x in range(10):
	print x, "is less than 10"

for x in range(10):
	if x == 3:
		continue 	# go immediately to the next iteration
	if x == 5:
		break 		# quit the loop entirely
	print x


#Truthiness
one_is_less_than_two = 1 < 2 		# equals True
true_equals_false = True == False	# equals False

	
x = None
print x == None 	# prints True, but is not Pythonic	
print x is None		# prints True, and is Pythonic


def some_function_that_returns_a_string():
	return "string_of_test"

s = some_function_that_returns_a_string()
if s:
	first_char = s[0]
else:
	first_char = ""


first_char = s and s[0]

safe_x = x or 0

print all([True,1,{3}])	#True
print all([True,1,{}])	#False, {} is falsy
print any([True,1,{}])	#True, True is truthy
print all([])		#True, no falsy elements in the list 
print any([])		#False, no truthy element in the list

 






