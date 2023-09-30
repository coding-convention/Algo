import sys
sysin = sys.stdin.readline

from collections import deque

def solve():
    p = sysin().rstrip()
    n = int(sysin())
    arr = deque(sysin().rstrip()[1:-1].split(','))

    if arr[0] == '':
        arr.pop()


    flag = 1

    for i in p:
        if i == 'R':
            flag *= -1
        
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                return
            
            if flag == 1:
                arr.popleft()

            elif flag == -1:
                arr.pop()

    print('[', end='')

    if flag == 1:
        l = len(arr)
        pp(arr)
    
    else:
        arr.reverse()
        pp(arr)

    print(']')
    
def pp(arr):
    l = len(arr)
    for i in range(l):
        print(arr[i], end='')
        if i != l-1:
            print(',',end='')



T = int(sysin())

for i in range(T):
    solve()