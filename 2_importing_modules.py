import random
print(random.__all__)

# can specify an alias for a module name
import random as r
print(r.__all__)

num = r.randint(5, 10)
print(num)

# can import all functions from a module
# beware name collisions
from random import *

num2 = randint(30, 90)
print(num2)

# import specific function names
from random import randrange
num3 = randrange(100, 121, 5)
print(num3)

# use an alias for function names
from random import randrange as rr
num4 = rr(250, 300, 10)
print(num4)
