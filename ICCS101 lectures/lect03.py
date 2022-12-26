"""
Lecture 3: Further Expressions

Announcements:
- A1 due Wed 11:59p (Thu 11:59p with a late day)
- A2 will be posted tomorrow
- Q1 is coming up next Tuesday (covering lect 1-4)



Topics
- printing with f-string
- string escaping
- built-in functions
- order of arithmetic operations: PEMDAS
- call expression
- operators are type-sensitive
- type conversion
- problem with type ambiguity
- booleans
- comparison operators
"""

# More about printing
# ---------
print('hello')
print('world')

# don't want a new line?
print('hello world')

s = 'hello'
t = 'world'
joined_string = s + ' ' + t

# name = 'sunsern'
# new_s = s + ' ' + name  # create a new variable called new_s that joins together s  ' '  name
print(joined_string)

# print multiple stuff
print(s, t)

# how about if i dont want to have a space between hello and world
s = 'hello'
t = 'world'
joined_string = s + t
# name = 'sunsern'
# new_s = s + ' ' + name  # create a new variable called new_s that joins together s  ' '  name
print(joined_string)

# Say if i want to print out 'one:two'
u = 'one'
v = 'two'
print(u, ':', v)
ans = u + ':' + v
print(ans)
print(u + ':' + v)  # you can print the result right away

# f-string -- formatted string
# --------
name = 'Jason'  # this is a normal string
template = f'Dear {name}, The value of 2 + 2 is {2 + 2}.'  # f-string
print(template)

s = 'Hello'
name = 'Sunsern'
print(f'{s} {name}')
print('{s} {name}')  # this is not an f-string

name = "Johnny"  # str
iphone_version = 14  # int
print(f"{name}'s phone is iphone {iphone_version}.")

a = 9
print(f'{a} + {2 * a} = {3 * a}')

# String escaping - How to print special characters
# ----------------

# print('I'm Sunsern')
print("I'm Sunsern")

# Hi, this is "iccs101" \\ 'icpy221'
print('Hi, this is \"iccs101\" \\\\ \'icpy221\'')

print('Hi, this is \"iccs101\" \\\\ \'icpy221\'')

# special characters: "   '   \
# have to be keyed in with special rule:  \"  \'  \\

print("Hi, this is \"iccs101\" \\\\ 'icpy221'")  # begin with " then do not need to escape '
print('Hi, this is "iccs101" \\\\ \'icpy221\'')  # begin with ' then do not need to escape "

text = f"Hi, this is \"iccs101\" \\\\ \'icpy221\'"
print(text)

# \n and \t are special sequences
# \n ==> newline
# \t ==> tab
new_text = 'hi\ta\nb\tc\nd\n'
print(new_text)

# \t -- tab character
# \n -- newline character
print('======\n\tHi\n======\n')

# Built-in functions -- pre-made functions that you can use right away
# ------------------
# 1. abs(x) -- returns absolute value of x (|x|)
# 2. round(x) -- returns the rounded version of x to the closest whole number
# 3. min()
# 4. max()

x = 25
y = abs(x)
print(y)

x = 0.4
y = round(x)
print(f'round({x})=', y)

x = 0.6
y = round(x)
print(f'round({x})=', y)

# round up to 1  or round down to 0  ==> 0  (even)
x = 0.5
y = round(x)
print(f'round({x})=', y)

# round up to 2 or round down to 1  ==> 2  (even)
x = 1.5
y = round(x)
print(f'round({x})=', y)

# round up to 3 or round down to 2  ==> 2  (even)
x = 2.5
y = round(x)
print(f'round({x})={y}')

# round(x, num_digits) -- rounds to the number of specified digits after the decimal point
# --------------------
x = 3.318317371937193719
y = round(x, 4)
print(y)

# min(x,y,...)  returns the minimum value of the arguments
# max(x,y,...)  returns the maximum value of the arguments
#  notes: things in parenthesis are known as arguments or parameters
# ------------
a = 10
b = 20
c = min(a, b, 100, -500, 2000)
d = max(a, b)
print(f'{a} {b} {c} {d}')

# Order of operations
# -----------------
x = 1 + 2 + 3 + 4
y = x * 2
z1 = 2 * 3 + 1  # viral meme/post: 7 or 8
z2 = 1 + 2 * 3
print(z1)
print(z2)

# Python follows PEMDAS
# 1. parentheses (P)
# 2. exponentiate (E) (**)
# 3. multiply(*) / divide(/,//) / Modulo(%) (MD)
# 4. add / subtract (AS)

# z = 2*3+1
'''
1. P: no
2. E: no     (**)
3. MD: yes   =>   z = (2*3)+1 = 6+1
4. AS: yes   =>   z = 6+1 = 7
'''

# z = 1+2*3
'''
1. P: no
2. E: no     (**)
3. MD: yes   =>   z = 1+(2*3) = 1+6
4. AS: yes   =>   z = 1+6 = 7

'''

# z = 7+6//2*3-2**2*(1+1)
'''
1. P: yes => z = 7+6//2*3-2**2*(1+1) = 7+6//2*3-2**2*2
2: E: yes => z = 7+6//2*3-(2**2)*2 = 7+6//2*3-4*2
3. MD: yes =>  z = 7+(6//2)*3-4*2 = 7+3*3-4*2
                 = 7+(3*3)-4*2 = 7+9-4*2
                 = 7+9-(4*2) = 7+9-8
4. AS: yes =>  z = (7+9)-8 = 16-8
                 = 16-8 = 8

'''
z = 7 + 6 // 2 * 3 - 2 ** 2 * (1 + 1)
print(z)

# Notes: when you code, use parentheses
# for example: instead of z = 2*3+1, write z = (2*3)+1
# common mistake: 9**1/2 == 4.5
#                 9**(1/2) == 3.0


# Break
# Back at 11.05


# Call expression
# ----------------
z = min(min(min(6, 7), max(1, 100)), max(abs(-7), max(3, 1)))
#       ___________________________  ________________________
#                arg1 = 6                arg2 = 7
# idea: first Python need to figure the VALUES of arg1 and arg2
'''
what is arg1? arg1 is min(min(6, 7), max(1, 100))
- we need to know min(6, 7) and max(1, 100) first! 
- yes, we know that min(6,7) is 6 and max(1,100) is 100
- so arg1 = min(6, 100) which is 6

what is arg2? arg2 is max(abs(-7), max(3, 1))
- arg2 = max(7, 3) = 7

So, z = min(arg1, arg2) = min(6, 7) = 6 
'''
print(z)

z = min(round(7.5) + 1, max(abs(10 - 20), 3 ** 2))
#        arg1=?     ,   arg2=?
# arg1 = round(7.5)+1 = 8+1 = 9
# arg2 = max(abs(10-20), 3**2) = max(10,9) = 10
# so, z is min(9,10) = 9

print(z)  # 9

# Python operators are type-sensitive
# -------------------------------
sum_num = 4 + 5  # add two numbers together
sum_str = 'hi' + 'bye'  # join (concatenation) string without any spaces
print(sum_num, sum_str)

hi = 10
what_is = 4 + 'hi'  # Error! cannot +: int and str
print(what_is)

four_hi = '4' + 'hi'
# or
four_hi = str(4) + 'hi'  # convert 4 into a string and then join with hi
# or
four_hi = f'{4}' + 'hi'  # first term is a string

# Takeaway: when you write an expression, be clear about the
# operator i.e. what you intend to do

mul_num = 4 * 5  # multiply 4 by 5
mul_str = 'hi' * 4  # repeats 'hi' 4 times
# what_is = 'hi' * 1.5  # this doesn't make sense in Python
# how_about = 'hi' * 'hey' # Error. cannot multiply a string by a string
print('yo' * (6 / 2))  # this doesnt make sense in python: 6/2 == 3.0 (float)
print('yo' * (6 // 2))  # this is good! 6//2 == 3 (int)
print(mul_num, mul_str)

# Type conversion
# ---------------
a = '3'  # type: str
# b = a + 5 # doesn't make sense to python: str + int
w = int(a)  # converting a to type int
b = w + 5  # OK. because int_a is an int
print(b)

x = input()  # type:str
print(x + 1)

x = int(input())  # type=int by using int() conversion
print(x + 1)

a = '1.5'
int_a = int(a)  # Error! '1.5' cannot be converted to an int
print(int_a + 10)

a = '2.0'
int_a = int(a)  # Error! '2.0' cannot be converted to an int
print(int_a + 10)

a = '2.0'
w = float(a)  # '2.0' into a float ==> w = 2.0
print(w + 10)  # float + int ==> float
# 12
# 12.0  <= correct
# error


a = '10'  # a = '10' type: str
w = float(a)  # w = 10.0 type: float
z = int(w + 10)  # w + 10 = 20.0  ==> int(20.0) => z = 20 (dropping the decimal points)
print(z * 2.0)  # z * 2.0 = 20 * 2.0 = 40.0
# what is the expected output?
# 40
# 20.0
# 40.0  <= correct
# error


# float to int conversion  - done by dropping the decimal points
f = 1.99999999  # this is a float
int_f = int(f)  # drop the decimal points. int_f = 1
print(int_f + 1)

p = 10
a = 'p'
print(int(a))

p = 10
a = p
print(int(a))

# int to str
a = 2  # a = 2 (int)
s = str(a)  # s = '2' (str)
print(s * 2)  # what is s*2? s repeated 2 times = '22'
# 4
# 22
# error
# ss

# what is the type of s*2? str!


# Q: so we can convert int-looking str to float but cannot
# convert float looking str to int?
# A: Correct!


# Type annotation -- mark type of variables
# ---------------
# 2 benefits:
#   1. for programmers, we're aware of the type of a variable
#   2. for python editor (pycharm), it can run real-time analysis about variables better
first: int = 10  # first is a variable of type int
second: int = 20  # second is a variable of type int
third: int = first * second  # type of third can be inferred by type of first and second

first: float = first / 1

a: int = 10
b: int = f'{a}'  # expected an int, but got a str instead
c = a + b

# Boolean (bool)
#   - Each boolean takes on two values: True / False

is_today_tuesday: bool = True
is_raining: bool = False
is_afternoon: bool = False

# ---------
# boolean expression
#  operators:
#  1.  and
#  2.  or
#  3.  not

# And --- truth table
#   True  and  True      == True
#   True  and  False     == False
#   False  and  True     == False
#   False  and  False    == False

# Ex:
is_today_tuesday: bool = True
is_raining: bool = True
is_afternoon: bool = False

# Q: is today tuesday AND raining?    True
# Q: is raining AND afternoon?  False

# Ex:
a = False
b = True
print(a and b)

# Ex:
is_today_tuesday: bool = True
is_raining: bool = False
is_afternoon: bool = False
print(is_today_tuesday and is_raining)

# Or  -- truth table
#   True  or  True      == True
#   True  or  False     == True
#   False  or  True     == True
#   False  or  False    == False

# Ex:
a = _____
b = False
print(a or b)  # True

# a must be True

# not --- truth table
#    not True  == False
#    not False == True


p: bool = True
q: bool = False
print((not p) or q)
# (not True) or False
# False or False
# False


p: bool = True
q: bool = ____
print((not p) and q)  # True

p: bool = True
q: bool = False
r = (p or q) and (q and q)
'''
(True or False) and (False and False)
    True        and       False
              False
'''
print(r)

# (p or q) and (q and q)
# (True or False) and (False and False)
#  -------------       ---------------
#     True                 False
#     --------------------------
#              False

# Comparators:
#   >    :   greater than
#   <    :   less than
#   ==   :   equal to    ***  note how equal to is == not = (assignment)
#   >=   :   greater than or equal to
#   <=   :   less than or equal to
#   !=   :   not equal
# ----------
p: bool = (10 > 8)  # True
q: bool = (5 % 3 == 0)  # 5 % 3 means the remainder of 5 divided by 3 which is 2, 2 == 0 is False
print(p and q)
# True and False == False


# we can write a boolean expression above like this:
r: bool = (10 > 8) and (5 % 3 == 0)
print(r)

u = (not (10 < 12)) or (not (1 == 5))
print(u)
'''
u = (not (10 < 12)) or (not (1 == 5))
  = (not True) or (not False)
  = False or True
  = True
'''

is_today_tuesday: bool = True
is_raining: bool = False
is_afternoon: bool = True

q1 = (not is_raining and (10 ** 2 % 10 > 0)) or (not is_afternoon and is_today_tuesday)
print(q1)
'''
q1 = (not is_raining and (10**2 % 10 > 0)) or (not is_afternoon and is_today_tuesday)
   = (not is_raining and (10**2 % 10 > 0)) or (not True and True)
   = (not is_raining and (10**2 % 10 > 0)) or False
   = (not False and (10**2 % 10 > 0))  # 10**2%10 ==> 100%10 ==> 0 > 0 ==> False
   = (not False and False) or False
   = (True and False) or False
   = False or False
   = False
'''

# equality with strings
is_raining: bool = True
q2 = (not ('a' == 'b')) and (('c' != 'a') or is_raining)
print(q2)
'''
q2 = (not ('a' == 'b')) and (('c' != 'a') or is_raining)
   = (not ('a' == 'b')) and (('c' != 'a') or True)
   = (not ('a' == 'b')) and True
   = (not False) and True
   = True and True 
   = True
'''
