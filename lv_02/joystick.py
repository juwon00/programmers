def solution(name):
    answer = 0

    i = 0
    a_cnt = 0
    a_max_cnt = 0
    a_max_loc = 0
    
    for x in name:
        if x == 'A':
            i += 1
            a_cnt += 1
            if a_cnt > a_max_cnt:
                a_max_cnt = a_cnt
                a_max_loc = i - a_max_cnt
        else:
            i += 1
            a_cnt = 0
    
    print(a_max_loc, a_max_cnt)
    print(len(name) - a_max_cnt - a_max_loc)
    
    if a_max_loc > 0:
        if a_max_loc < len(name) - a_max_cnt - a_max_loc:
            print('f')
            answer = 2 * (a_max_loc - 1) + (len(name) - a_max_cnt - a_max_loc)
        else:
            if a_max_loc > 1:
                print('b')
                answer = 2 * (len(name) - a_max_cnt - a_max_loc) + (a_max_loc - 1)
            else:
                print('bb')
                answer = 1
    else:
        if name in 'A':
            answer = len(name) - 1
        else:
            answer = len(name) - 1
    
    # ! 양 옆으로 움직이는 회로 다시 생각해야됨 
     
    
    
        
    for y in name:
        if ord(y) <= 77:
            print("FFF", ord(y) - 65)
            answer += ord(y) - 65
        else:
            print("BBB", 90 - ord(y) + 1)
            answer += 90 - ord(y) + 1
    
    
    return answer



print(solution("ZAA"))



# M-13 N-13