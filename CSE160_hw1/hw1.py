# Name: Michael Shieh 1826962
# CSE 160
# Winter 2020
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and then copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all of the problems given.

# Uncomment the line below to make the math.sqrt function available
import math

# Problem 1

print("Problem 1 solution follows:")

a = 3
b = -5.86
c = 2.5408
print("Root 1:", ((-1)*b + math.sqrt(b**2 - 4*a*c))/2*a)
print("Root 2:", ((-1)*b - math.sqrt(b**2 - 4*a*c))/2*a, "\n")


# Problem 2
print("Problem 2 solution follows:")

for num in range(2, 11):
    print("1/" + str(num) + ":", float(1)/num)
print("")

# Problem 3
print("Problem 3 solution follows:")

n = 10
triangular = 0
for num in range(1, n+1):
    triangular = triangular + num
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2, "\n")

# Problem 4
print("Problem 4 solution follows:")

n = 10
factorial = 1
for num in range(1, n+1):
    factorial = factorial * num
print("10!:", factorial, "\n")

# Problem 5
print("Problem 5 solution follows:")
n = 10
for num1 in range(n, 0, -1):
    factorial = 1
    for num2 in range(1, num1+1):
        factorial = factorial * num2
    print(str(num1) + "!:", factorial)
print("")

# Problem 6
print("Problem 6 solution follows:")

n = 10
sum = 1
for num1 in range(n, 0, -1):
    factorial = 1
    for num2 in range(1, num1+1):
        factorial = factorial * num2
    sum = sum + 1/factorial
print("e:", sum, "\n")

# Collaboration

# ... Write your answer here, as a comment (on lines starting with "#").
