# 자동완성

class Node():
    def __init__(self, key) -> None:
        self.key = key
        self.children = {}
        self.cnt = 0

class Trie():
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head
        for char in string:
            curr_node.cnt += 1
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.cnt += 1

    def auto_perfection(self, string):
        curr_node = self.head
        where = 0
        for char in string:
            if curr_node.cnt == 1:
                # slice를 포함한 단어가 유일하면 지금까지의 문자개수 return
                return where
            
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                where += 1
            else:
                # 이 경우는 존재하지 않음.
                return False
        
        return where
                

def solution(words):
    answer = 0

    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        # print(word, trie.auto_perfection(word))
        answer += trie.auto_perfection(word)

    return answer

words = ["go","gone","guild"]
print(solution(words))