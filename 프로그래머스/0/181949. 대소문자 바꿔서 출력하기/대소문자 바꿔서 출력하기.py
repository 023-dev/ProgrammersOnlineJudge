str = list(input())
rtn = ''
for i in str:
    if i.islower():
        rtn += i.upper()
    else:
        rtn += i.lower()
print(rtn)