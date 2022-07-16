from sys import exit

x, y = input("Enter X and Y (x, y): ").replace(" ", "").split(',')

try:
    x, y = int(x), int(y)
except Exception:
    print("Please enter in numbers!")
    exit()

matrix = []

for i in range(x):
    column = []
    for j in range(y):
        column.append(i*j)
    matrix.append(column)

print(matrix)