matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(matrix[0][0])
print(matrix[2][1])

for row in matrix:
    for col in row:
        print(col)
