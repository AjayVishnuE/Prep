# ... Two Dimensional Lists(arrays) ...

# Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements, find the index position of the maximum element and print two numbers representing the index (i×j) or the row number and the column number. If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number.

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)

# Given an odd number integer n, produce a two-dimensional array of size (n×n). Fill each element with a single character string of "." . Then fill the middle row, the middle column and the diagnals with the single character string of "*" (an image of a snow flake). Print the array elements in (n×n) rows and columns and separate the characters with a single space.

n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

# Given two numbers n and m. Create a two-dimensional array of size (n×m) and populate it with the characters "." and "*" in a checkerboard pattern. The top left corner should have the character "." .

a = input().split()
n, m = int(a[0]), int(a[1])
a = []
b = ". " * m
for i in range(n):
    a.append(b.split(" "))
for i in range(n):
    for j in range(m):
        if (i+j)%2 != 0:
            a[i][j] = "*"
for i in range(n):
    print(" ".join(a[i]))

# Given an integer n, produce a two-dimensional array of size (n×n) and complete it according to the following rules, and print with a single space between characters:
# On the main diagonal write 0 .
# On the diagonals adjacent to the main, write 1 .
# On the next adjacent diagonals write 2 and so forth.
# Print the elements of the resulting array.

n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))

# Given an integer n, create a two-dimensional array of size (n×n) and populate it as follows, with spaces between each character:
# The positions on the minor diagonal (from the upper right to the lower left corner) receive 1 .
# The positions above this diagonal recieve 0 .
# The positions below the diagonal receive 2 .
# Print the elements of the resulting array.

n = int(input())
ls = []
for i in range(n):
    a = [[0]*(n-i-1) + [1] + [2] * i]
    ls.append(a)
for i in range(n):
    for j in ls[i]:
        print(' '.join([str(i) for i in j]))

# Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.
# Write a function swap_columns(a, i, j) and call it to exchange the columns.

def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))

# Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by one integer c, multiply every entry of the matrix by c and print the result.
 
m, n = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
c = int(input())
for i in range(m):
    for j in range(n):
        A[i][j] *= c
print('\n'.join([' '.join([str(k) for k in row]) for row in A]))

# Given three positive integers m, n and r, m lines of n elements, giving an m×n matrix A, and n lines of r elements, giving an n×r matrix B, form the product matrix AB, which is the m×r matrix whose (i,k)  entry is the sum A[i][1]∗B[1][k]+⋯+A[i][n]∗B[n][k] and print the result.

m, n, r = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
B = [[int(k) for k in input().split()] for j in range(n)]
C = [[0]*r for i in range(m)]
for i in range(m):
    for k in range(r):
        for j in range(n):
            C[i][k] += A[i][j] * B[j][k]
print('\n'.join([' '.join([str(k) for k in row]) for row in C]))
