print 'Hello World'

#####################
# Unit 13.3
#####################

##Comments
# this is a comment
# place this at the top of python file to enable running as >>./filename.py
#####! /usr/bin/python
# otherwise you can run with >>python filename.py {or} >>python27 filename.py
# those commands can be run from a terminal window

###Variable Types
int_val = 8
long_val = 23423423235L
float_val = 2.0
bool_val = True
##Input	Output
print "Variable type examples:"
print type(int_val)
print type(long_val)
print type(float_val)
print type(bool_val)

# testing for the type of a variable
print(isinstance(float_val, float))
print(isinstance(float_val, int))

#####################
# 13.3.2 Arithmetic and Casting
#####################

print "\nArithmetic examples:"
print 8 / 3
print float(8) / 3
print float(8) / float(3)

print True and False  # logicals	False
print 8 == 3  # logical equality	False
print 5 <= 6  # logical comparison	True

print 2.0 * 4.0  # multiplication	8.0
print 65 % 6  # remainder, modulus	5
print 3 ** 4  # 3 to the fourth power	81

#####################
# 13.3.3 Strings and String Operations
#####################

print "\nString Example"

str_val = "A string is double or single quotes"
print str_val

str_val_long = '''Three quotes means that the string goes over
multiple lines'''
print str_val_long

# this did not work...
str_val_no_newline = '''This also spans multiple lines
\ but has no new line'''
print str_val_no_newline

# string can be accessed in a variety of different ways

print str_val

print str_val[0]  # initial element "0th" element	A

print str_val[3:5]  # elements 3 and 4, but not 5	tr

print str_val[-1]  # the last element in the string	s

print str_val[-5:]  # the last five elements	uotes

print str_val[0:5] + '  ' + str_val[5:]  # print the first five elements, then from the fifth and on

#  some common operations for strings

print str_val * 2  # multiply is like adding many times; here it repeats the string            A string is double or single quotesA string is double or single quotes

print 'Python' > 'Java'  # compare the strings alphabetically

print "eric".capitalize()  # the dot operator works like most other OOP languages

print str_val.lower()

print str_val.upper()

print "this, is, separated, by, commas".split(
    ',')  # this result is returned as a list, which we need to talk about!      ['this', 'is', 'separated', 'by', 'commas']

a = 'Databases are great!'
b = "'Databases are great!'"

print a[3:8] + a[9:10]
print b[3:6] + b[-1]

#####################
# 13.3.4 Lists and Tuples
#####################

# a list is one of the most powerful tools in Python from which
# most abstract types are created and implemented
# a list is very much like the mutable version of a tuple
# it can hold any type of information
a_list = [45, 67, "not a number"]

# we can add to a list through the append function
a_list.append("A string, appended as a new element in the list")
print a_list

# lists can have other lists in them
tmp_list = ["a list", "within another list", 442]
a_list.append(tmp_list)
print a_list

# all of the indexing we learned from before still works with lists
print a_list[-1]
print a_list[-2:]

# tuples are immutable lists and are designated by commas
# you can store ANYTHING inside a tuple; it's basically a complex object container
a_tuple = 45, 67, 'not a number'
print a_tuple

# you can access a tuple with square brackets
print a_tuple[2]

# but you cannot change a tuple; it's immutable!!


fruit_list = ['apple', 'orange', 'lime', 'pear', 'tomato']
fruit_list.pop()
fruit_list.pop()
fruit_list.pop()
fruit_list.insert(2, 'lemon')
fruit_list.insert(2, 'lemon')
fruit_list.append('in the coconut')

print(fruit_list)


#####################
# 13.3.5 Python Sets
#####################

# Sets, taken from the Python sets tutorial
# https://docs.python.org/2/tutorial/datastructures.html#sets
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)  # create a set without duplicates,
print fruit
print 'orange' in fruit  # fast membership testing	True
print 'crabgrass' in fruit

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a.add('!')  # also add some punctuation

# set operations
print a
print a - b  # unique letters in a
print a | b  # letters in a but not b
print a & b  # letters in either a or b
print a ^ b  # letters in a or b but not both


fruit_list = set(['apple', 'orange', 'lime', 'pear', 'tomato'])
fruit_list &= set(['tomato','lemon', 'papaya'])
print fruit_list


#####################
# 13.3.6 Python Dictionaries
#####################

# dictionaries map keys to values
# here we set up a key as a string and the value as a number
num_legs = {'dog': 4, 'cat': 4, 'human': 2}
 
# you access subscripts via the "key"
print num_legs
print num_legs ['dog']
print num_legs ['human']
# again, these are just containers for any memory type
num_legs['human'] = 'two'
num_legs['bird'] = 'two and some wings'
num_legs[45] = 'a key that is not a string'
# the key can be any immutable memory
 
del num_legs ['cat']
print num_legs


#####################
# 13.4 Python Loops
#####################

# ============================================
# for loop example with list
print "\nfor loop output:"

list_example = [int_val, long_val, float_val, bool_val]
list_example.insert(0, "DataMining")

# notice that the loop ends with a colon and
# is designated by the tab alignment
for val in list_example:
    print str(val) + ' ' + str(type(val))
    print "This statement is in the loop"



# you can also get the index using the enumerate example
for index, val in enumerate(list_example):
     print str(val), '\t is at index \t', index


# say you have two lists of equal size, that you would like to
# loop through without indexing, you can use the "zip" function
questions = ['name', 'the holy grail', 'blue']
answers = ['lancelot', 'quest', 'favorite color']
for q,a in zip(questions, answers):
     print 'What is your %s? It is %s.' % (q,a)

# Looping through dictionaries	===============
print '==============='
# Get all the keys	bird => two and some wings
print num_legs.keys()

for k in num_legs.keys():
    print k, "=>", num_legs[k]

print '==============='
# you can also use the iter_items function	bird => two and some wings
for k, v in num_legs.iteritems():
    print k, "=>", v

print '==============='
# Test for presence of a key
for t in ['human', 'beast', 'cat', 'dog', 45]:
    print t
    if num_legs.has_key(t):
        print '=>', num_legs[t]
    else:
        print 'is not present.'


#####################
# 13.4.2 Comprehensions
#####################

# imagine we want to take every element in a range to the fourth power
times_four = [x ** 4 for x in range(10)]
print times_four

# you can also call functions inside a comprehension
questions = ['name', 'quest', 'favorite color']
quest_upper = [x.upper() for x in questions]
print quest_upper

# you can also do comprehensions with dictionaries
times_four = {x: x ** 4 for x in range(10)}
# notice curly braces and key placement
print times_four

# all of the enumerate, zipping, and slicing we performed also applies to
# list comprehensions
x_array = [10, 20, 30]
y_array = [7, 5, 3]
# this prints the sum of the multiplication of the arrays
print sum(x*y for x,y in zip(x_array, y_array))


list_output = [x for x in 'databases']
print list_output
