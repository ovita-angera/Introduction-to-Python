string = '0123456789'

matrix = [[string[i] for i in range(len(string))] for _ in range(len(string))]

for row in matrix:
    print(row)
