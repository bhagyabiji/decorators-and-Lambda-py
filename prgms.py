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

