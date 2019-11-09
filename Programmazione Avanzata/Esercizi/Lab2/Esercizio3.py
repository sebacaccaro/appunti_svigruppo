""" sin(x) can be approximate by the Taylor's series:


Let's write a library to implement sin(x, n) by using the Taylor's series 
(where n is the level of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).

Let's compare your function with the one implemented in the math module at the growing of the approximation level.

Hint. Use a generator for the factorial and a comprehension for the series. """
from functools import reduce
from math import factorial as factorial1
import time


def factorial(firstNumber=1, step=2, n=1000):
    factorial = reduce((lambda x, y: x * y), range(1, firstNumber+1))
    currentStep = step
    currentNumber = firstNumber + 1
    for i in range(0, n*step):
        if (currentStep == step):
            yield(factorial)
            step = 0
        factorial = factorial * currentNumber
        step += 1
        currentNumber += 1


def sign(n=1000):
    s = 1
    for i in range(0, n):
        yield s
        s = -s


def sequenceTerm(step=2, n=1000):
    term = 1
    for i in range(0, n):
        yield term
        term += step


def values(n=1000):
    f = factorial(1, 2, n)
    s = sign(n)
    t = sequenceTerm(2, n)
    for i in range(5, n):
        print(i)
        yield (next(f), next(s), next(t))


def sin(x, n):
    return sum([(s*(x**t))/f for (f, s, t) in values()])


def taylor(x, n):
    return sum([((-1)**i)*(x**(2*i+1))/factorial1(2*i+1) for i in range(n)])


start_time = time.time()
#print(sin(1, 2))
print(taylor(1, 1000))
print("--- %s seconds ---" % (time.time() - start_time))
