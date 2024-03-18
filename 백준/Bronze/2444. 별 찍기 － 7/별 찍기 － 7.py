import sys
num = int(sys.stdin.readline())
star = ''
for i in range(1,2*num):
    if i <=  num:
        star += (" "*(num-i)) + ("*"*(2*i-1))
    else:
        star += (" "*(i-num)) + ("*"*((2*num-1)-2*(i-num)))
    star += '\n'
print(star)