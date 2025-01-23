class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        def find_root(word):
            node = root
            prefix = []
            for char in word:
                if char not in node.children:
                    break
                prefix.append(char)
                node = node.children[char]
                if node.is_end_of_word:
                    return "".join(prefix)

            return word

        words = sentence.split()
        result = [find_root(word) for word in words]
        return " ".join(result)
