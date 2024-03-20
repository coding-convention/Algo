from itertools import combinations
from collections import deque


def mkGraph(begin, words):
    graph={begin:[]}
    words.append(begin)
    for word in words:
        graph.setdefault(word, [])
        
    def isEdge(v1, v2):
        l = len(v1)
        count = 0
        for i in range(l):
            if v1[i]!=v2[i]:
                count += 1
                if count == 2:
                    break
        if count == 1:
            return True
        else:
            return False
        
    for v1, v2 in combinations(words, 2):
        if isEdge(v1, v2):
            graph[v1].append(v2)
            graph[v2].append(v1)
        
    return graph

def bfs(begin, target, graph):
    chk = {}
    for k in graph.keys():
        chk.setdefault(k, 0)
    
    q = deque([begin])
    while q:
        curr = q.popleft()
        for v in graph[curr]:
            if chk[v] == 0:
                chk[v] = chk[curr] + 1
                q.append(v)
#            	q.append(v)
                # print(test)

                if v == target:
                    return chk[v]
    return 0
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    graph = mkGraph(begin, words)
    
    answer = bfs(begin, target, graph)

    return answer