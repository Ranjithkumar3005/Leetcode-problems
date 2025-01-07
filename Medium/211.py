class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False  # Indicates if the node marks the end of a word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):  # If we've processed all characters
                return node.isEnd  # Check if it's the end of a valid word

            char = word[index]
            if char == ".":
                # Try all possible child nodes
                for child in node.children.values():
                    if dfs(
                        child, index + 1
                    ):  # Recursively check for remaining characters
                        return True
                return False
            else:  # Regular character case
                if char not in node.children:
                    return False  # Character not present in Trie
                return dfs(node.children[char], index + 1)  # Move to the next node

        return dfs(self.root, 0)  # Start the search from the root
