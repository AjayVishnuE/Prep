# ...While loop...


# For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.

n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2, end=" ")
    i += 1

# Given an integer not less than 2. Print its smallest integer divisor greater than 1.

n=int(input())
i=2
while(i<=n):
    if n%i==0:
        print(i)
        break
    i+=1

# For a given integer N, find the greatest integer x where 2x is less than or equal to N. Print the exponent value and the result of the expression 2x.
# Don't use the operation **.

n=int(input())
i=0
while(2**i<=n):
    temp=i
    i+=1
print(temp,2**temp)

# As a future athlete you just started your practice for an upcoming event. Given that on the first day you run x miles, and by the event you must be able to run y miles.
# Calculate the number of days required for you to finally reach the required distance for the event, if you increases your distance each day by 10% from the previous day.
# Print one integer representing the number of days to reach the required distance.

x = int(input())
y = int(input())
count = 1
while x < y:
  x += x * 0.1
  count += 1
print(count)

# Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence, where the sequence ends when the integer is equal to 0. Print the length of the sequence (not counting the integer 0). The numbers following the number 0 should be omitted.

n=int(input())
count=0
while(1):
    if n==0:
        print(count)
        break
    else:
        count+=1
        n=int(input())
   
# Determine the sum of all elements in the sequence, ending with the number 0.

x=int(input())
sum=x
while(x!=0):
    x=int(input())
    sum+=x
print(sum)

# Determine the average of all elements of the sequence ending with the number 0.

n=int(input())
count=sum=0
while(n!=0):
    count+=1
    sum+=n
    n=int(input())
print(sum/count)

# A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence.

n=int(input())
large=0
while(n!=0):
    if n>large:
        large=n
    n=int(input())
print(large)

# A sequence consists of integer numbers and ends with the number 0. Determine the index of the largest element of the sequence. If the highest element is not unique, print the index of the first of them.

n=int(input())
largei=0
numlar=0
count=0
while(n!=0):
    if numlar<n:
        numlar=n
        largei=count
    count+=1
    n=int(input())
print(largei+1)

# Determine the number of even elements in the sequence ending with the number 0.

n=int(input())
count=0
while(n!=0):
    if n%2==0:
        count+=1
    n=int(input())
print(count)

# A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above.

n=int(input())
m=int(input())
count=0
while(m!=0):
    if m>n:
        count+=1
    n=m
    m=int(input())
print(count)

# The sequence consists of distinct positive integer numbers and ends with the number 0. Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.

l=[]
n=int(input())
while(n!=0):
    l.append(n)
    n=int(input())
l=sorted(l)
print(l[len(l)-2])

# A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element.

n=int(input())
l=[]
while(n!=0):
    l.append(n)
    n=int(input())
l=sorted(l)
x=l[len(l)-1]
count=0
for i in range(len(l)-1,-1,-1):
    if x==l[i]:
        count+=1
print(count)

# The Fibonacci sequence is defined as follows: ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# Given a non-negative integer n, print the nth Fibonacci number ϕn.
# This problem can also be solved with a for loop.

n=int(input())
previousFib = 0
currentFib = 1
if n <= 1:
    print(n)
else:
    for i in range(n - 1):
        newFib = previousFib + currentFib
        previousFib = currentFib
        currentFib = newFib
    print(currentFib)

# The Fibonacci sequence is defined as follows: ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# Given an integer a, determine its index among the Fibonacci numbers, that is, print the number n such that ϕn=a. If a is not a Fibonacci number, print -1.

a=0
b=1
c=1
i=1
check=0
n=int(input())
while(c<=n):
    c=a+b
    a=b
    b=c
    i+=1
    if c==n:
        print(i)
        check=1
if check==0:
    print(-1)

# Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other.

x = int(input())
prev = x
count = 1
mcount = count
while x != 0:
  x = int(input())
  if x == prev:
    count += 1
    prev = x
  else:
    if count > mcount:
      mcount = count
    count = 1
    prev = x
print(mcount)

