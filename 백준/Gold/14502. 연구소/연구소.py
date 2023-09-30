from collections import deque
from copy import deepcopy

import sys
sysin = sys.stdin.readline

def Count(lab:list) -> int:
    c = 0
    for i in lab:
        for j in i:
            if not j:
                c += 1
    return c

def Spreading(lab:list, size:tuple, wall) -> list:
    visited = deepcopy(lab)
    for i, j in wall:
        visited[j][i] = 1

    queue = deque()
    N, M = size
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 2:
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()
        for j, i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= x + i < M and 0 <= y + j < N and not visited[y+j][x+i]:
                visited[y+j][x+i] = 2
                queue.append((y+j, x+i))
    
    return visited

# N = 세로 M = 가로
N, M = map(int, sysin().split())

lab = [ list(map(int, sysin().split())) for _ in range(N)]

empty = []
for i in range(N):
    for j in range(M):
        if not lab[i][j]:
            empty.append((j, i))

length = len(empty)
answer = 0
for i in range(0, length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            contaminated = Spreading(lab, (N, M), (empty[i], empty[j], empty[k]))
            c = Count(contaminated)
            if answer < c:
                answer = c

print(answer)