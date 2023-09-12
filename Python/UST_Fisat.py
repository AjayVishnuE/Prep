## Calculate the count of perfect squares in an integer array.

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

## Calculate the Square of the negative elements in an array

# SOLUTION 

import math

n=int(input("Enter Array Length: "))
l = [int(input("Enter Array: "))for i in range(n)]

for i in range(n):
    if(l[i] < 0):
        l[i]=l[i]**2
print(l)

## Remove vowels from the end until a constant occurs and return the rest of the string.Both lower and upper case are included

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

## Given an integer N, check if Divisible by 5, if yes, divide it by 5, If not divisible by 5, check for divisibility by 3. If yes divide by 3. If not, repeat checking and division with respect to 2, If none of the above cases, decrement number by 1. Continue the process until num=0 and display number of steps taken for the same

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