n = int(input())
matrix = [ ]
for i in range(n):
    row = [ ]
    for x in input().split(' '):
        row.append(int(x))
    matrix.append(row)
s = int(input())

for row in range(n):
    for col in range(n):
        matrix[row][col] *= s

for row in range(n):
    for col in range(n):
        if col != n - 1:
            print(matrix[row][col], end = ' ')
        else:
            print(matrix[row][col])