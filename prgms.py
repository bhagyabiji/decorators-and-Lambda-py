#Decorator example
    #A basic decorator that uppercases the return value of the decorated function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase  #changecase fn is a decorator
def myfunction():
  return "Hello Sally"

print(myfunction())

print("------------")

#Using the @changecase decorator on two functions
def myfun(funct):
  def inner():
    return funct().upper()
  return (inner)

@myfun
def goodmrng():
  return "good mrng"

@myfun
def hello():
  return "helllo welcome"

print(goodmrng())
print(hello())

print("------------")

#Functions with arguments can also be decorated
def argu(func):
  def inn(x):
    return func(x).upper()
  return inn

@argu
def argmnt(n):
  return "hello " + n

print(argmnt("john"))

print("------------")

#lambda
x = lambda a : a+6
print(x(2))

m = lambda a,b : a*b 
print(m(2,3))

p = lambda r,s,t : r+s+t
print(p(4,6,2))

print("---------------")

def myfunc(n):
  return lambda a: a*n
mydouble = myfunc(2)
print(mydouble(11))

print("------map()---------")

num = [2,4,6,8]
doubled = list(map(lambda a: a*2, num))
print(doubled)

print("-------filter()--------")

#Filter out odd numbers from a list
numb = [1,7,2,4,5,3,8,11]
odd = list(filter(lambda x : x%2 !=0, numb))
print(odd)


print("-------sorted()--------")

#Sort a list of tuples by the second element
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sort_stud = sorted(students, key = lambda x: x[1])
print(sort_stud)

#Sort strings by length
str = ["apple", "pie", "banana", "cherry"]
sort_str = sorted(str, key = lambda a: len(a))
print(sort_str)



print("---------------")

#factorial
def factorial(n):
  #base case
  if n==0 or n==1:
    return 1
  #recursive case
  else:
    return n*factorial(n-1)
print(factorial(5))

print("---------------")

#fibonacci series
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))

print("---------------")

#Calculate the sum of all elements in a list
def sun(n):
  if len(n) == 0:
    return 0
  else:
    return n[0] + n[1:]

my_list = [1,2,3,4,5]
print(sum(my_list))

import sys
print(sys.getrecursionlimit())

print("-------------")

#Generator that yields numbers
def num_count(n):
  count = 1
  while count<=n:
    yield count
    count += 1

for num in num_count(5):
  print(num)


print("----------------")

#next() generator
def simple_gen():
  yield "Happy"
  yield "Birthday"
  yield "To You"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

print("----------------")

list_comp = [x*x for x in range(5)]
print(list_comp)

gen_exp = (x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))

print("----------------")

#Create a range of numbers from 0 to 9
x = range(3,10)
print(x)
print(list(x))

print("----------------")

print(list(range(5)))

print("----------------")

r = range(10)
print(r[2])
print(r[:3])

m = range(0, 10, 2)
print( 6 in r)
