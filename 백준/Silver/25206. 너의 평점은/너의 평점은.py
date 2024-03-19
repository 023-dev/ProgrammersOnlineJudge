import sys
dic = {
    "A+" :	4.5,
    "A0" :	4.0,
    "B+" :	3.5,
    "B0" :	3.0,
    "C+" :	2.5,
    "C0" :	2.0,
    "D+" :	1.5,
    "D0" :	1.0,
    "F" :	0.0  
}
prd, sum, n = 0.0, 0.0, 20
for i in range(n):
    subjects = list(sys.stdin.readline().split())
    if subjects[2] in dic:
        prd += float(dic[subjects[2]]) * float(subjects[1])
        sum += float(subjects[1])
print(float(prd)/float(sum))