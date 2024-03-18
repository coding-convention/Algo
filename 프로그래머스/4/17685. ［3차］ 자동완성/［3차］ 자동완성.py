class Node:
    def __init__(self):
        self.count = 0
        self.child = {}
        
class Trie:
    def __init__(self, words):
        self.root = {}
        self.add(words)
        
    def add(self, words):
        for word in words:
            curr = self.root
            for letter in word:
                curr.setdefault(letter, Node())
                curr[letter].count += 1
                curr = curr[letter].child
        
def solution(words):
    answer = 0
    trie = Trie(words)
    
    for word in words:
        curr = trie.root
        for letter in word:
            answer += 1
            if curr[letter].count == 1:
                break
            else:
                curr = curr[letter].child
    
    return answer