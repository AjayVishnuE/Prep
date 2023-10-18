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

#



#



#



#



#



#



#


