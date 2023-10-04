# ... Integer and float numbers ...

# Given an integer number, print its last digit.

a = int(input())
print(a% 10)

# Given an integer. Print its tens digit.

a=int(input())
a=a//10
print(a%10)

# Given a three-digit number. Find the sum of its digits.

n=int(input())
sum=0
while(n>0):
    temp=n%10
    sum+=temp
    n//=10
print(sum)

# Given a positive real number, print its fractional part.

n=input()
x="0"
check=0
for ele in n:
    if(check==1):
        x+=ele
    if(ele=="."):
        x+=ele
        check=1
print(x)

# Given a positive real number, print its first digit to the right of the decimal point.

n=input()
check=0
for i in range(len(n)):
    if(n[i]=="."):
        print(n[i+1])
        check=1
if(check==0):
    print("0")

# A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

n=int(input())
m=int(input())
res=m//n
if(m%n>0):
    print(res+1)
else:
    print(res)

# Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

a=int(input())
h=a//60
m=a%60
print(h,m)

# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

a=int(input())
b=int(input())
c=int(input())
d=a*c
s=b*c
if(b*c>99):
    d+=(s//100)
    s=s%100
print(d,s)

# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.

h=int(input())
m=int(input())
s=int(input())
mi=h*30+m*0.5+s*0.00833333
print(mi)

# Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

a=float(input())
a=a%30
print(a*12)




