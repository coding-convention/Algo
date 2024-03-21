def solution(n, tops):
    dp1 = [0] * n
    dp2 = [0] * n
    if tops[0] == 0:
        dp1[0] = 2
    
    elif tops[0] == 1:
        dp1[0] = 3
    dp2[0] = 1
    
    for i in range(1, n):
        if tops[i] == 0:
            dp1[i] = (dp1[i-1] * 2 + dp2[i-1]) % 10007
            dp2[i] = (dp1[i-1] + dp2[i-1]) % 10007
        else:
            dp1[i] = (dp1[i-1] * 3 + dp2[i-1] * 2) % 10007
            dp2[i] = (dp1[i-1] + dp2[i-1]) % 10007
    answer = dp1[n-1] + dp2[n-1]
    return answer % 10007