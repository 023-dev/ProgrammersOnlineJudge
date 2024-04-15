def solution(s, n):
    answer = ''
    print(ord('A'),ord('Z'),ord('a'),ord('z'))
    for i in s:
        if 64 < ord(i) and ord(i) < 91 and ord(i)+n>90:
            answer += chr(ord(i)+n-26)
        elif 96 < ord(i) and ord(i) < 123 and ord(i)+n>122:
            answer += chr(ord(i)+n-26)
        elif ord(i) == 32:
            answer += i
        else:
            answer += chr(ord(i)+n)
    return answer