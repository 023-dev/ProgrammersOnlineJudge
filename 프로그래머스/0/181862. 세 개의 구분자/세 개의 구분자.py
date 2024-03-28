import re
def solution(myStr):
    answer = list(filter(None, re.sub(r'[abc]', ' ', myStr).split(' ')))
    if not(len(answer)):
        answer.append('EMPTY')
    return answer