# ... Conditions: if, then, else ...

# Given two integers, print the smaller value.

a = int(input())
b = int(input())
print( min(a,b) )

# For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.

x=int(input())
if x==0:
    print("0")
elif x>0:
    print("1")
else:
    print("-1")

# Given three integers, print the smallest value.

a=int(input())
b=int(input())
c=int(input())
print(min(a,b,c))

# Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("3")
elif a==b or a==c or b==c:
    print("2")
else:
    print("0")

# Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a==c or b==d:
    print("YES")
else:
    print("NO")

# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

h1 = int (input()) 
w1 = int (input()) 
h2 = int (input())
w2 = int (input()) 
if ((h1 % 2 != 0) and (w1 % 2 != 0)) or ((h1 % 2 == 0) and (w1 % 2 == 0)):
    one = str ('black')
else:
    one = str ('white')
if ((h2 % 2 != 0) and (w2 % 2 != 0)) or ((h2 % 2 == 0) and (w2 % 2 == 0)):
    two = str ('black')
else:
    two = str ('white')
if one == two:
    print ('YES')
else:
    print ('NO')

# Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if abs(a-c)<2 and abs(b-d)<2:
    print("YES")
else:
    print("NO")

# In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
# The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a+b == c+d or b-a==d-c:
    print("YES")
else:
    print("NO")

# Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if  a==c or b==d or a+b==c+d or b-a == d-c:
    print("YES")
else:
    print("NO")

# Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.

col = int(input())
row = int(input())
colN = int(input())
rowN = int(input())
if (colN == col + 1 or colN == col - 1) and (rowN == row - 2 or rowN == row + 2):
  print ("YES")
elif (rowN == row + 1 or rowN == row - 1) and (colN == col - 2 or colN == col + 2):
  print ("YES")
else:
  print ("NO")

# Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
# The program reads three integers: n, m, and k. It should print YES or NO.

n = int(input())
m = int(input())
k = int(input())
if (k % n == 0 and k / n < m) or (k % m == 0 and k / m < n):
    print('YES')
else:
    print('NO')

# Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.

n = int(input())
if n%400==0:
    print("LEAP")
elif n%100==0:
    print("COMMON")
elif n%4 == 0:
    print("LEAP")
else:
    print("COMMON")



