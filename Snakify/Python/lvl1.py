# ... Input, print and numbers ...


# Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.

a=input()
print("Hi "+ a)

# Write a program that takes a number and print its square.

a=int(input())
print(a**2)

# Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.

b = int(input())
h = int(input())
print(0.5 * b * h)

# Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. 

name = input()
print('Hello, ',name,"!", sep="")

# N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above.

n = int(input())
a=int(input())
print(a//n)
print(a % n)

# Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.
# Remember that you can convert the numbers to strings using the function str.

a = int(input())
b=(a+1)
c=(a-1)
print('The next number for the number ', a ,' is ' , b ,'.', sep="")
print('The previous number for the number ', a ,' is ' , c ,'.', sep="")

# A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.

h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

h1=h1*3600
m1=m1*60

h2=h2*3600
m2=m2*60

time1=h1+m1+s1
time2=h2+m2+s2

print(time2-time1)

# A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

first = int(input())
second = int(input())
third = int(input())
if first%2==0:
    avg1=first/2
else:
    avg1=(first//2)+1

if second%2==0:
    avg2=second/2
else:
    avg2=(second//2)+1
    
if third%2==0:
    avg3=third//2
else:
    avg3=(third//2)+1

print(int(avg1+avg2+avg3))


