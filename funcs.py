# Lab 2 Functions
# Name: Tyler Baxter
# Section: 3
import math


# 1) purpose statement: This function computes a given formula
# signature: int, int -> float
def do_math(x, y):
    return (x ** 2 - 3 / 5 * x * y ** 2) / ((2 * x ** 2 * y) / 5 + 4)


# 2) purpose statement: This function computes one solution of the quadratic formula
# signature: int, int, int -> float
def quadratic_formula1(a, b, c):
    return (-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


# 3) purpose statement: This function computes the other solution of the quadratic formula
# signature: int, int, int -> float
def quadratic_formula2(a, b, c):
    return (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


# 4) purpose statement: This function finds the Manhattan distance between two points
# signature: int, int, int, int -> float
def distance(x1, y1, x2, y2):
    return math.fabs(x1 - x2) + math.fabs(y1 - y2)


# 5) purpose statement: This function determines if a number is positive
# signature: int -> boolean
def is_positive(num):
    return num > 0


# 6) purpose statement: This function determines if a number is divisible by 7 without remainder
# signature: int -> boolean
def dividable_by_7(num):
    return num % 7 == 0


