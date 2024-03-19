import sys
borad = [['']*15 for i in range(5)]
str = ''
for x in range(5):
    row = input()
    for y in range(len(row)):
        borad[x][y] = row[y]
for y in range(15):
    for x in range(5):
        str += borad[x][y] 
print(str)