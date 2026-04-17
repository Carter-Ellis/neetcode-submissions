#
#
#   Given a 2-D grid of chars (board) and a list of strings (words), return all words that are present in the grid.
#
#   Notes:
#       - Words can only be formed by horizontal or vertical neighboring cells.
#       - The same cell may not be used more than once IN A WORD.
#     
#   Variables:
#   global res = []    
#   
#   rec function vars:    
#       visited = set() => (coordinates)
#       subStr = ""
#
#   Input:
#   board = [
#       ["a","b","c","d"],
#       ["s","a","a","t"],
#       ["a","c","k","e"],
#       ["a","c","d","n"]
#   ],
#   words = ["bat","cat","back","backend","stack"]
#   Output: ["cat","back","backend"]
#
#

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ROW, COL = len(board), len(board[0])
        res = []

        def rec(curr, row, col, subStr, visited):
            if (not curr or (row, col) in visited or row >= ROW or col >= COL or row < 0 or col < 0):
                return
            
            c = board[row][col]
            
            if c not in curr.children:
                return
            curr = curr.children[c]

            subStr += c
            visited.add((row, col))
            if curr.isWord and subStr not in res:
                res.append(subStr)

            rec(curr, row + 1, col, subStr, visited)
            rec(curr, row - 1, col, subStr, visited)
            rec(curr, row, col + 1, subStr, visited)
            rec(curr, row, col - 1, subStr, visited)
            visited.remove((row,col))

        for r in range(ROW):
            for c in range(COL):
                rec(trie.root, r, c, "", set())

        return res
            









