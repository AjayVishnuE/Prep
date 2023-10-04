# ... Strings ...

# You are given a string.
# In the first line, print the third character of this string.
# In the second line, print the second to last character of this string.
# In the third line, print the first five characters of this string.
# In the fourth line, print all but the last two characters of this string.
# In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
# In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
# In the seventh line, print all the characters of the string in reverse order.
# In the eighth line, print every second character of the string in reverse order, starting from the last one.
# In the ninth line, print the length of the given string.

s=str(input())
l=len(s)
print(s[2])
print(s[l-2])
print(s[0:5])
print(s[0:l-2])
for i in range(l):
    if i % 2==0:
        print(s[i],end="")
print()
for i in range(l):
    if i % 2!=0:
        print(s[i],end="")
print()
print(s[::-1])
for i in range(l-1,-1,-2):
    print(s[i],end="")
print()
print(l)

# Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.

count=1
str=input()
for i in range(len(str)):
    if str[i]==" ":
        count+=1
print(count)

# Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, so that the first string contains one more characther than the second). Now print a new string on a single row with the first and second halfs interchanged (second half first and the first half second)
# Don't use the statement if in this task.

from math import ceil
lst = list(str(input("Enter the word: ")))
h = ceil(len(lst) / 2)
r = lst[h:] + lst[:h]
print(''.join(r))

# Given a string consisting of exactly two words separated by a space. Print a new string with the first and second word positions swapped (the second word is printed first).

check=0
l1=[]
l2=[]
s=input()
for i in s:
    if i==" ":
        check=1
    if check==0:
        l1.append(i)
    else:
        l2.append(i)
print("".join(l2), "".join(l1),sep=" ")

# Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then do not print anything.

s=e=0
st=input()
count=-1
for i in range(len(st)):
    if st[i]=="f" and count==-1:
        s=i
        count+=1
    elif st[i]=="f" and count>-1:
        e=i
        count+=1
if count==0:
    print(s)
elif count>0:
    print(s,e)
    
# Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence of the letter f. If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2.

s=input()
count=-2
for i in range(len(s)):
    if s[i]=="f":
        count+=1
    if count==0 and s[i]=="f":
        c=i
if count<0:
    print(count)
else:
    print(c)
    
# Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.       

s=input()
x=len(s)
check=0
for i in range(x):
    if s[i]=="h" and check==0:
        check=1
        start=i
    elif check==1 and s[i]=="h":
        end=i
print(s[0:start],s[end+1:x],sep="")

# Given a string in which the letter h occurs at least two times, reverse the sequence of characters enclosed between the first and last appearances.

s=input()
check=0
start=end=0
n=len(s)
for i in range(n):
    if check==0 and s[i]=="h":
        start=i
        check=1
    elif check==1 and s[i]=="h":
        end=i
x=s[start:end]
print(s[0:start+1],x[::-1],s[end+1:n],sep="")

# Given a string. Replace in this string all the numbers 1 by the word one.

s=str(input())
l=[]
for i in range(len(s)):
    if s[i] == "1":
        l.append("one")
    else:
        l.append(s[i])
print("".join(l))

# Given a string. Remove from this string all the characters @.

s=input()
l=[]
for ele in s:
    if ele!="@":
        l.append(ele)
print("".join(l))

# Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.

s=input()
n=len(s)
check=0
l=[]
for i in range(n):
    l.append(s[i])
    if s[i]=="h":
        end=i
for i in range(n-1,-1,-1):
    if s[i]=="h":
        start=i
for i in range(start+1,end,1):
    if l[i]=="h":
        l[i]="H"
print("".join(l))

# Given a string. Delete from it all the characters whose indices are divisible by 3.

s=input()
l=[]
for i in range(len(s)):
    if i%3==0:
        pass
    else:
        l.append(s[i])
print("".join(l))


