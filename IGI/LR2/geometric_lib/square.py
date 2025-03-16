import os

def area(a):
    return a * a


def perimeter(a):
    return 4 * a
val = input("Enter the length of a square: ")

perim = perimeter(int(val))
print(perim)