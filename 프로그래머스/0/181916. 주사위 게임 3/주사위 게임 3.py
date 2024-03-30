def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    dice_case = len(set(dice))
    acc, cnt = 0, 0
    # 네 주사위에서 나온 숫자가 모두 p로 같다면
    if dice_case == 1:
        return 1111 * dice[0]
    # 주사위 숫자 개수가 2개
    elif dice_case == 2:
        acc = max(dice, key = dice.count)
        cnt = dice.count(acc)
        dice.sort()
        # 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q라면
        if cnt == 3:
            return pow(10*dice[dice.index(acc)]+dice[dice.index(min(dice, key = dice.count))],2)
        # 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q라고 한다면
        elif cnt == 2:
            return (dice[0]+dice[-1])*abs(dice[0]-dice[-1])
    # 두 주사위에서 나온 숫자가 p로 같고 나머지 주사위에서 나온 숫자가 각각 q, r 이라면 
    elif dice_case == 3:
        acc = max(dice, key = dice.count)
        dice.remove(acc)
        dice.remove(acc)
        return dice[0] * dice[-1]
    # 네 주사위에 적힌 숫자가 모두 다르다면
    elif dice_case == 4:
        return min(dice)
    return answer