import math
import sys
sys.setrecursionlimit(99999)


# Print the sum of all number to 1000 divisible for 3 and 5
print(sum((filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(1001)))))

# Calculate the sum of the figures of 2^1000
print(sum([int(char) for char in str(2 ** 1000)]))

# MCM between first 20 numbers


def mcd(a, b):
    return (b > a and mcd(b, a)) or (a % b == 0 and b) or mcd(b, a % b)


def mcm(a, b):
    return int((a*b)/mcd(a, b))


def mcmInRange(maxRange=20):
    return (maxRange <= 1 and 1) or mcm(mcmInRange(maxRange - 1), maxRange)


print("Mcm 1-20", mcmInRange())

# Calculate the first term in the Fibonacci sequence to contain 1000 digits


def fibonacci(x=0, y=1):
    return (math.ceil(math.log(x+y, 10))+1 >= 1000 and x + y) or fibonacci(y, x + y)


print(fibonacci())
