import math
import random
from decimal import *
minimum = int( input ("What is the lower bound?"))
maximum = int( input ("What is the upper bound?"))
numbers = int( input ("How many numbers do you want to generate?"))
for count in range(numbers):
    print(random.randint(minimum,maximum))