from typing import List


class MagicDictionary:

    def __init__(self):
        self.h = []

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.h.append(i)

    def search(self, searchWord: str) -> bool:
        for i in self.h:
            if len(i) != len(searchWord):
                continue
            c = 0
            for j in range(0, len(i)):
                if searchWord[j] != i[j]:
                    c += 1
                if c == 2:
                    break
            if c == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
