from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        que = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while que:
            curr_word, curr_len = que.popleft()
            for i in range(len(curr_word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new_word = curr_word[:i] + j + curr_word[i + 1 :]
                    if new_word == endWord:
                        return curr_len + 1
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        que.append((new_word, curr_len + 1))
        return 0
