def solution(polynomial):
    answer = ''
    arr = polynomial.split()
    x_val, n_val = 0, 0
    tmp = ''
    for i in range(len(arr)):
        tmp = arr[i]
        if i % 2 == 0:
            if tmp[-1] == 'x':
                if tmp == 'x':
                    x_val += 1
                else:
                    x_val += int(tmp[0:-1])
            else:
                n_val += int(tmp)
    if x_val > 0 and n_val < 1:
        if x_val > 1:
            answer = str(x_val) + 'x'
        else:
            answer = 'x'
    elif x_val < 1 and n_val > 0:
        answer = str(n_val)
    elif x_val > 0 and n_val > 0:
        if x_val > 1:
            answer = str(x_val) + 'x + ' + str(n_val)
        else:
            answer = 'x + ' + str(n_val)
    else:
        answr = '0'
    return answer