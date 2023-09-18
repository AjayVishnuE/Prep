## 1...Calculate the count of perfect squares in an integer array.

# SOLUTION 

import math

n=int(input("Enter Array Length: "))
l = [int(input("Enter Array: "))for i in range(n)]
count = 0 

for ele in l:
    x = math.sqrt(ele)
    if (x % 1 ==0 ):
        count += 1
print("No. of Perfect Squares In Array:",count)

## 2...Calculate the Square of the negative elements in an array

# SOLUTION 

import math

n=int(input("Enter Array Length: "))
l = [int(input("Enter Array: "))for i in range(n)]

for i in range(n):
    if(l[i] < 0):
        l[i]=l[i]**2
print(l)

## 3...Remove vowels from the end until a constant occurs and return the rest of the string.Both lower and upper case are included

# SOLUTION - 1

vowels = ['a','e','i','0','u']      
length=len(str1)
ans,ans1,sol=[],[],[]
str1= list(input().lower())

for i in range(length-1,-1,-1):
    if(str1[i].isdigit()):
        print("".join(ans))
        break
    elif(str1[i] not in vowels):
        ans.append(str1[i])

for j in range(i):
    sol.append(str1[j])
    
ans1=ans[::-1]
sol=sol+ans1
print("".join(sol))

# SOLUTION - 2

n=list(input().lower())
vowel =['a','e','i','o','u']
length = len(n)
for i in range(length-1,-1,-1):
    if(n[i].isdigit()):
        print("".join(n))
        exit(0)
    elif(n[i] in vowel):
        n.pop(i)

## 4...Given an integer N, check if Divisible by 5, if yes, divide it by 5, If not divisible by 5, check for divisibility by 3. If yes divide by 3. If not, repeat checking and division with respect to 2, If none of the above cases, decrement number by 1. Continue the process until num=0 and display number of steps taken for the same

# SOLUTION 

N = int(input())
num=N
count=0
while(num!=0):
    if num % 5 == 0:
        num/=5
    elif num % 3 == 0:
        num/=3
    elif num % 2 == 0:
        num/=2
    else:
        num-=1
    count+=1
print(count)

## 5...In an array A,find the absolute difference of the two adjacent elements and store it in array B.Find the sum of (B[i] xor i) and return the value of the sum modulous 10^9*7

# SOLUTION 

n=int(input("Length of Array: "))
l1=[int(input("Enter The Array: ")) for i in range(n)]
l2=[]
sum1=0
l2.append(l1[0])

for i in range(0,len(l1)-1):
    l2.append(abs(l1[i]-l1[i+1]))
    
for i in range(0, len(l2)):
    sum1 += l2[i] ^ i
    
print(sum1%(10**9*7))

## 6...In array input from the user, remove even numbers and repeated numbers. Then display the size of array after the removal of these elements.

# SOLUTION 

n=int(input("Length of Array: "))
l1=[int(input("Enter The Array: ")) for i in range(n)]
l2=[]

for ele in l1:
    if(ele % 2 != 0 and ele not in l2):
        l2.append(ele)
print(l2)

## 7...Given an array A of array_size of integers with numbers that can be repeated or be negative,find the smallest and largest prime number and take the absolute difference of the smallest and largest prime number

# SOLUTION 

small=large=0
flag1=flag2=0
n=int(input("Enter the Size of Array: "))
print("Enter the Array:")
L1 = [int(input()) for i in  range(n)]

L1.sort()
print(L1)

for j in range(n):
    
    if (flag1==0 and L1[j]>1):
        count=0
        for k in range(1, L1[j]):
            if(L1[j]%k==0):
                count+=1
        if(count <= 1):
            small=L1[j]
            flag1=1
            
    if (flag2==0):
        count=0
        for k in range(1,L1[n-j-1]//2):
            if(L1[n-j-1]%k==0):
                count+=1
        if(count <= 1):
            large=L1[n-j-1]
            flag2=1
            
print(small,large)

## 8...Reverse a number

# SOLUTION 

n=int(input())
rev=0
while(n>0):
    temp=n % 10
    rev = rev*10+temp
    n//=10
print(rev)

## 9...Given a string S(Length of S>=10) with digits, alphabets, etc. Return the last 10 digit number in the string as a string.Example: Input:987-af-6-gj-1234567891-r Output:1234567891

# SOLUTION 

l1 = list(input())
l2=[]
for ele in l1:
    if ele.isdigit():
        l2.append(ele)
        
if(len(l2)<10):
    for i in range(len(l2),11,1):
        l2.append(0)
    
print("".join(l2[-10:]))

## 10...Given an array of size n for each element in the array convert it to binary remove the last 2 bits and again convert it to decimal. Do this for all the elements of the array and then find the sum. If the sum is a large number then apply modulo 10^9+7 on it and return the sum

# SOLUTION 

n=int(input())
l1 = [int(input()) for i in range(n)]
sum1=0

for ele in l1:
    temp=list(bin(ele))
    l=len(temp)
    temp = temp[0:-2]
    str1=""
    for elem in temp:
        str1=str1+elem
    if(str1=="0b"):
        val=0
    else:
        val=int(str1,2)
    sum1=sum1+val
print(sum1)

## 11...Define a function to return the absolute difference between the largest and the smallest prime number in the given array. The array may contain any integer, positive or negative. Negative numbers, 0 and 1 in the array are not to be considered.

# SOLUTION 

## 12...Given an array of integers. For each pair of adjacent elements, take first element as length and second as breadth. Find area and perimeter(of rectangle) for each pair. If area is greater than perimeter, it is type A couple. If area is lesser than perimeter, it is type B couple. Return the absolute difference between the number of type A and type B couples.

# SOLUTION 

## 13...

# SOLUTION 

## 14...

# SOLUTION 

## 1...

# SOLUTION 









