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

