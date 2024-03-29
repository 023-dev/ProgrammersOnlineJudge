def solution(str_list):
    answer = []
    try:
        if str_list.count('r') and str_list.count('l'):
            l_idx = str_list.index('l')
            r_idx = str_list.index('r')
            if l_idx < r_idx:
                answer = str_list[:l_idx]
            else:
                answer = str_list[r_idx+1:]
        elif str_list.count('l'):
            answer = str_list[:str_list.index('l')]
        else:    
            answer = str_list[str_list.index('r')+1:]
        return answer
    except ValueError:            
    	return answer