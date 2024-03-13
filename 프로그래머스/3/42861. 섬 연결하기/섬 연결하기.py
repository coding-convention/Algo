def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    mask = set([costs[0][0]])
    while len(mask) != n:
        for c in costs:
            if not((c[0] in mask) ^ (c[1] in mask)): 
                continue
            else:
                mask.update(c[:2])
                answer += c[2]
                break
    return answer