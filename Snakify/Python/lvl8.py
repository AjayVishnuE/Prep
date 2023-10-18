# ... Functions and recursion ...

# Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2). Write a function distance(x1, y1, x2, y2) to compute the distance between the points (x1,y1) and (x2,y2). Read four real numbers and print the resulting distance calculated by the function. The formula for distance between two points can be found at Wolfram.

def distance(x1, y1, x2, y2):
    import math
    dx = (x2-x1)
    dy = (y2-y1)
    distance = math.sqrt((dx**2) + (dy**2))
    return distance
print(distance(float(input()), float(input()), float(input()), float(input())))

# Given a positive real number a and integer n. Compute a^n. Write a function power(a, n) to calculate the results using the function and print the result of the expression. Don't use the same function from the standard library.

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
print(power(float(input()), int(input())))

# Write a function capitalize(lower_case_word) that takes the lower case word and returns the word with the first letter capitalized. Eg., print(capitalize('word')) should print the word Word. Then, given a line of lowercase ASCII words (text separated by a single space), print it with the first letter of each word capitalized using the your own function capitalize(). In Python there is a function ord(character), which returns character code in the ASCII chart, and the function chr(code), which returns the character itself from the ASCII code. For example, ord('a') == 97, chr(97) == 'a'.

def capitalize(a):
    st = a.split(" ")
    nst = []
    for i in range(len(st)):
        b = st[i]
        c = b[0].upper() + b[1:len(st[i])]
        nst.append(c)
    return(" ".join(nst))
print(capitalize(input()))

# Given a positive real number a and a non-negative integer n. Calculate an without using loops, ** operator or the built in function math.pow(). Instead, use recursion and the relation an=a⋅an−1. Print the result. Form the function power(a, n).

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)
a = float(input())
n = float(input())
print(power(a, n))

# Given a sequence of integers that end with a 0. Print the sequence in reverse order. Don't use lists or other data structures. Use the force of recursion instead.

def reverse():
    a = int(input())
    if a != 0:
        reverse()
    print(a)
reverse()

# Given a non-negative integer n, print the nth Fibonacci number. Do this by writing a function fib(n) which takes the non-negative integer n and returns the nth Fibonacci number. Don't use loops, use the flair of recursion instead. However, you should think about why the recursive method is much slower than using loops.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(int(input())))

