"""
Lecture 2: Getting Started with Python
Announcements:
- A1 is posted
  - How to submit and how to verify your submission
- Q0 (on Canvas) ASAP
- Make sure to preview/review lessons before/after each lecture
Topics
- code vs comments
- print statement
- syntax error
- values & types
- variables
- basic math in python
- strings
- taking input from user
"""
# Comments:
#  comments start with # symbol
#  this is a comment and Python interpreter ignores this line
"""
block comment:
when you have a long text to write
you can use this
"""
'''
Another block comment:
blah
'''
# Print statement
# ---------------
print('abc')
print("abc")
print("Hello World!")
print('Hello World! (with single quotes)')
# ctrl + / for block comment
print('1')
print('2')
print("3")
# The following line has a problem
print('hello')
print(hello)
# Types & Values: Data in Python
# ----------------
#  "hello"     -  type:  str     (strings / text)
#  25          -  type:  int     (integers / whole numbers)
#  3.0         -  type:  float   (floating points / real numbers)
"""
76    <- Type: int,  Value: 76
5.0   <- Type: float, Value: 5 | 5.0 
3.14  <- Type: float, Value: 3.14
0     <- Type: int,   Value: 0
'yo'  <- Type: str,   Value: yo 
'0'   type:str   value: '0'
0.0   type:float value: 0
"""
print('hello') # you can print a string
print(3.0) # you can print a float
print(25)  # you can print an int
print('25')
# '25' -- this is a string
# ctrl + / to do block comment/uncomment
# you can print multiple items. each item will be
# separated by ' ' and they appear on the same line
print(10, 20, 30)
print('a', 5, 1.2)
# "3" -> Type: str  , Value: "3"
# Variables
# ---------------
#  - alias for some data
#  - named location in memory (RAM)
x = 10   # define a variable x, set it to 10
# Q: what is the type of the data that x is referring to?
# A: int
# Q: what is the value of the data that x is referring to?
# A: 10
# when you have a variable, you can ask about: 1) its value 2) its type
# in this case, x has the value of 10 and x has type int
y = 'thanks'
x = 5.0  # redefine x to be 5.0
"""
y   <- Type: str  Value: 'thanks'
x   <- Type: float Value: 5.0
"""
a = 1
b = 2
a = 7
b = a # when a variable is on RHS, python will look up current value and
      # replace it with the data.
      # this line becomes: b = 7
print(b,a)
# Variable naming
# ----------------
#  Python variables:
#   1. cannot start with a number nor a punctuation
#   2. _ (underscore) is allowed
#   3. are case-sensitive
"""
911t     <-- invalid
+8-a     <-- invalid
_911t    <-- valid
?hi      <-- invalid
__       <-- valid
"""
_7eleven = 10 # valid
seven11 = 711 # valid
seven_11 = 711  # valid
7eleven = 711  # invalid
seven-eleven = 711  # invalid
seven_eleven = 711  # valid
# Case sensitivity
a = 'A'
A = 'a'  # this is not the same variable as above
print(a)
print(A)
seveneleven = 711
sevenEleven = 711
SevenEleven = 711
# the above three variables are 3 different variables
# 9x = 10  # this is invalid variable name
# !x = 30  # this is also invalid
_test = 25  # this is ok
t_est = 89  # this is ok too
t3s1 = 199  # this is ok as well
# Advice: name your variable with a meaningful name
# Break
# Resume at 11:05
# Variable Namespace
# ------------------
# once you define a variable, it is available to
# the whole program
# print(x)
# update the value of x
x = 20
print(x)   # prints out 20
x = 30
print(x)   # prints out 30
# Math in Python
y = x + 10  # y = 30 + 10
print(y)    # see 40
x = x + 20  # x = 30 + 20 = 50
print(x)    # see 50
# Introducing Python console
# -----
#  - REPL -- read-eval-print loop
# Math operators
# -------------
#   +    add
#   -    subtract
#   *    multiply
#   /    divide (float) -- give float results
#   //   divide (int) , floor division
#   **   exponentiation ( to the power of ) e.g. 3**2
#   %    modulo,  remainder. a%b gives the reminder of a divided by b
#         For example:  4%3 -->  1   because  4/3 => 1 + 1/3
# floor example
# --------
# floor(1.3) == 1         1  ----  1.3  --------------- 2
# floor(1.6) == 1         1  ----------------1.6 -------2
# floor(2.0) == 2
# floor(0.5) == 0         0               0.5           1
# floor(-1.5) == -2       -2 ----------- -1.5 -------- -1
# floor(-2) == -2
# -10//3 ~ -3.33         -4 ---------------- -3.33 ---- -3
# Strings
# -------
#  sequence of characters
fruit = "grape"
print(fruit)
# extract a single character by giving its position (index)
# In python, the first character has the index 0
#  g r a p e
#  0 1 2 3 4
first = fruit[0]  # first = 'g'
print(first)
print(fruit[0])
# or
letter = fruit[3]
print(letter)
# the number of characters in a string by using len()
l = len(fruit)    # len( <some string> ) gives the length of the string
print(l)
fruit = 'durian'
l2 = len(fruit)
print(l2)
# type() command
# -------------
#  this is to show type of a value
print(type(fruit))
print(type(10))
print(type(4.6))
# Type conversion
# -------------
age = 87  # this is int
age_text = str(age)   #  str( <some value> ) converts the value into string
print(age_text, type(age_text))
print('first digit of age', age_text[0])
# print(age[0])  # this is invalid because you cannot index an int
# Taking input from user
# ---------------------
a = input()
b = input()
print(a, type(a))
print(b, type(b))
c = input('Enter c: ')  # prompt message
d = input('Enter d: ')
print(type(a))
print(type(b))
num = input('Num:')  # currently a string
num = int(num)  # now an int
print(num)
# or
num = int(input('Num: '))
