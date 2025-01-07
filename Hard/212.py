from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        found_words = set()
        visited = [[False] * cols for _ in range(rows)]

        def backtrack(r, c, node, path):
            char = board[r][c]
            if char not in node.children:
                return

            visited[r][c] = True
            node = node.children[char]
            path += char

            if node.isEnd:
                found_words.add(path)

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    backtrack(nr, nc, node, path)

            visited[r][c] = False

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie.root, "")

        return list(found_words)
