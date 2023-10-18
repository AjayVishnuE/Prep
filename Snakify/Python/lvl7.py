# ... Lists ...

# Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...).

a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

# Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range()

a = [int(i) for i in input().split()]
for elem in a:
    if elem % 2 == 0:
        print(elem)

# Given a list of numbers, find and print all the elements that are greater than the previous element.                                                                                                               

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank.

st = input().split()
for i in range(len(st)-1):
    if int(st[i]) * int(st[i+1]) > 0:
        print(st[i], st[i+1], end = " ")
        break

# Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors. The first and the last items of the list shouldn't be considered because they don't have two neighbors.

a = [int(i) for i in input().split()]
n = 0
for i in range(1,len(a)-1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        n += 1
print(n)

# Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the index number. If the highest element is not unique, print the index of the first instance.

a = [int(i) for i in input().split()]
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(max, a.index(max))

# Given a list of numbers with all of its elements sorted in ascending order, determine and print the quantity of distinct elements in it.

a = [int(i)for i in input().split()]
n = 1
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        n += 1
print(n)

# Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element in place.

a = [int(i) for i in input().split()]
n = 0
for i in range(int(len(a)/2)):
    a[n],a[n+1] = a[n+1],a[n]
    n += 2
for i in a:
    print(i, end = " ")

# Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list.

a = [int(i) for i in input().split()]
max = a[0]
min = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
l = a.index(max)
m = a.index(min)
a[l],a[m] = a[m], a[l]
for i in a:
    print(i, end =" ")

# Given a list of numbers, count how many element pairs have the same value (are equal). Any two elements that are equal to each other should be counted exactly once.

a = [int(i) for i in input().split()]
n = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            n += 1
print(n)

# Given a list of numbers, find and print the elements that appear in the list only once. The elements must be printed in the order in which they occur in the original list.

a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end = " ")

# In chess it is known that it is possible to place 8 queens on an 8×8 chess board such that none of them can attack another. Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other on the next move. Print the word NO if no queen can attack another, otherwise print YES. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chess board with rows and columns numbered starting at 1.

a = []
for i in range(8):
    ls = [int(i) for i in input().split()]
    a.append(ls)
n = 0
for i in range(8):
    for j in range(i+1,8):
        if abs(a[i][1]-a[j][1]) == abs(a[i][0]-a[j][0]):
            n += 1
        elif abs(a[i][1]-a[j][1]) == 0 or abs(a[i][0]-a[j][0]) == 0:
            n += 1
        else:
            n += 0
if n == 0:
    print("NO")
else:
    print("YES")


# In bowling, the player starts wtih 10 pins at the far end of a lane. The object is to knock all the pins down. For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled. The balls are numbered from 1 to N (inclusive) for this situation. The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins that were knocked down with each role. Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down.

n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))

