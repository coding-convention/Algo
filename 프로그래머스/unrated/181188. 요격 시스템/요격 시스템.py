def solution(targets):
    targets.sort(key = lambda x:[x[1], x[0]])
    answer = 1
    
    flag = targets[0][1]
    
    for t in targets:
        if flag <= t[0]:
            flag = t[1]
            answer += 1
    
    return answer