class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        h = {}
        for i in chars:
            if i not in h:
                h[i] = chars.count(i)
        print(h)
        strs = ""
        count = 0
        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                if words[i][j] in h:
                    if h[words[i][j]] >= words[i].count(words[i][j]):
                        count += 1
                    else:
                        break
                else:
                    break
            if count == len(words[i]):
                strs += words[i]
            count = 0
        return len(strs)
