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


#####################
# 13.4.3 Stacks and Queues
#####################

####### list as a stack
print "\nStack Example:"
list_example = []
list_example.append('LIFO')

for i in range(0, 5):
    list_example.append(i)

print list_example

val = list_example.pop()

print val
print list_example

######## list as a queue
print "\nQueue Example:"
from collections import deque

# this is an import, we will get back to that later

q_example = deque()
q_example.appendleft("FIFO")
for i in range(5, 10):
    q_example.appendleft(i)

print q_example

val = q_example.pop()
print val
print q_example


#####################
# 13.4.4 Conditionals
#####################

# conditional example
print "\nConditional Example:"
a, b = True, False

if a:
    print "a is true"
elif a or b:
    print "b is true"
else:
    print "neither a or b is true"

# conditional assignment
val = "b is true" if b else "b is false"
print val

# I. The traditional == works as expected
a=5
b=5
if a==b:
     print "I. Everybody is a five!"
else:
     print "I. Wish we had fives..."

# II. The "is" function is for object comparison, much like comparing pointers
a=327676
b=a
if a is b:
     print "II. These are the same object!"
else:
     print "II. Wish we had the same objects..."

# III. While these have the same value, they are not the same memory
a=327676
b=327675+1
if a is b:
     print "III. These are the same object!"
else:
     print "III. Wish we had the same objects..."

# IV. You would expect this to say "Wish we had fives...", but small integers
# like this are cached, so right now they do point to the same memory
a = 5
b = 4 + 1
if a is b:
    print "IV. Everybody is a five!"
else:
    print "IV. Wish we had fives..."

# V. But if we change the memory, that caching gets released
b = b * 2.0
b = b / 2.0
if a is b:
    print "IV. Everybody is a five!"
else:
    print "IV. Wish we had fives..."


# you can also perform nested conditionals, like bounding
if 5 < 8 < 6: # not true because 8 is not less than 6
    print 'VI. How did we get here?'
elif 4 < 18 < 22:
    print 'VI. Got through nested conditional'


a = 3 < 7 < 32
print a
b = 'six' < 'seven'
print b
x = 10
print x
y = 9+1
print y
c = (x==y)
print c
d = (x is y)
print d
x = 567
print x
y = 566 + 1
print y
e = x is y
print e


#####################
# 13.5 Functions and Introspection
#####################

# create and call a function
# the function can be defined almost anywhere in file, as long as it is defined before it gets used
def make_strings_lowercase(str_input):
    assert isinstance(str_input, str)  # test the type of input
    return str_input.lower()


# now we are back on the main execution	Function Example:
print make_strings_lowercase("UPPER CASE")
print make_strings_lowercase("Data Mining")

#################
def show_data(data):
    print data


some_data = [1, 2, 3, 4, 5]
show_data(some_data)


# you can also define default values for the functions
def show_data(data, x=None, y=None):
    # print the data
    print data
    if x is not None:
        print x
    if y is not None:
        print y


some_data = [1, 2, 3, 4, 5]
show_data(some_data);
show_data(some_data, x='cool X value')
show_data(some_data, y='cool Y value', x='cool X value')


# as well as have multiple return types in the function
def get_square_and_tenth_power(x):
    return x**2, x**10
print get_square_and_tenth_power(2)

#####################
# 13.5.2 Classes
#####################

# This is a class that inherits from a generic object
class BodyPart(object):
    # this is a class variable, shared across all instances
    def __init__(self, name):
        self.name = name
        # the name attribute is unique to each instance of the class


# now define a class that subclasses from the defined BodyPart class
class Heart(BodyPart):
    def __init__(self, rate=60, units="minute"):
        self.rate = rate
        self.units = units
        super(Heart, self).__init__("Heart")

    def print_rate(self):
        print " name: " + str(self.name) + " has " + str(self.rate) + " beats per " + self.units


class BodyPart(object):
    kind = "This is a long string meant to be so long that the memory for it is not cached by python"
    # this is a class variable, shared across all instances

my_heart = Heart(1, "second")
generic_part = BodyPart("Foot")

print my_heart.kind

print my_heart.kind is generic_part.kind

#####################
# 13.5.3 Exception Handling
#####################

import random

i = random.randrange(0, 8)
j = random.randrange(-1, 6)
print i, j

some = [3, 10, 0, 8, 18];
try:
    den = some[j] / i
    print "A:", den
    frac = (i + j) / den
    print "B:", frac
    if frac = < 2:
        k = 3
    else
        k = 'mike'
    print "C:", k
    print "D:", some[k]
except ZeroDivisionError:
    print "\nDivision by zero."
except TypeError, detail:
    print "\nSome type mismatch:", detail
except IndexError, detail:
    print "\nSome value is out of range:", detail
except:
    print "\nSomething else went wrong."
else:
    print "\nThat's odd, nothing went wrong."


def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print "\nDivision by zero"

print safe_divide(1000,0)


#####################
# 13.5.4 Opening a File/"with" Command
#####################

# the regular way of opening a file, lots of error checking
try:
    file = open("some_file.txt")
    data = file.read()
except IOError, detail:
    print "\nCould not read file:", detail
else:
    print "Read successfully, file contents:"
    print data
finally:
    # this always gets called, close the file if it's open
    if not file.closed:
        file.close()



#####Opening a File Using "with"
with open("some_file.txt") as file:
    data = file.read()
    print "Read successfully, file contents:"
    print data

# is the file closed? Let's check.
print file.closed


####Writing a Class to Use "with"
class BodyPart(object):
    def __init__(self.name):
        self.name = name
        print'1. Just initialized body part with name', name

def __enter__(self):
    print '2. Building up from "with" command'
    return self

def __exit__(self, type, value, traceback):
    if value is not None:
        print '4. An error occurred,', value
    else:
        print '4. Exit was called, no errors'

def print_self(self):
    print '3. Hi, my name is:', self.name


with BodyPart("Lungs") as bp:
    bp.print_self()


import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end-self.start
        print('Code took %#.03f sec. to run' % self.interval)

with Timer() as t:
    1+1
    time.sleep(2)
    1 + 1
    time.sleep(2)
    1 + 1
    time.sleep(2)

print t

import numpy as np
t = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * t)

print np.max(y)
print np.median(y)

from matplotlib import pyplot as plt

plt.plot(t,y)
plt.show()


import sqlite3
print sqlite3.version

import pdb
j = 0
for i in range(0,5):
    j += 5*i
    pdb.set_trace()

print j


a = 5/2
b = 6/0
c = 5.0/2.0

type(a)
type(b)
type(c)

frozenset(["nights, ni"])
["nights, ni"]



for i in range(5):
    val = val + 2
    if val > 9:
        break
    else:
        val = None


x = 10
y = 9 + 1
c = (x == y)

d = (x is y)
print(c)
print(d)

print(20.0/40)