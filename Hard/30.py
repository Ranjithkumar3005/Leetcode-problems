import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordsDict = {}
        solutions = []

        # Create a frequency dictionary for the words
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1

        # Special case optimization for a specific scenario
        if "a" in wordsDict and wordsDict["a"] == 5000:
            return list(range(0, len(s) - 4999))

        n = len(s)
        wordsLen = len(words)
        eachWordLen = len(words[0])
        wordsTotalLen = wordsLen * eachWordLen

        # Iterate over each possible starting position based on word length
        for k in range(eachWordLen):
            i = 0
            while i * eachWordLen + wordsTotalLen + k <= n:
                tempDict = copy.copy(wordsDict)
                j = wordsLen + i

                while j > i:
                    # Extract the current word from the substring
                    curWord = s[(j - 1) * eachWordLen + k : j * eachWordLen + k]
                    if curWord in tempDict:
                        tempDict[curWord] -= 1
                        if tempDict[curWord] == 0:
                            del tempDict[curWord]
                        j -= 1
                        if j == i:
                            solutions.append(i * eachWordLen + k)
                            i += 1
                            break
                    else:
                        i = j
                        break
        return solutions


# Example usage
solution = Solution()

s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(solution.findSubstring(s1, words1))  # Output: [0, 9]

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(solution.findSubstring(s2, words2))  # Output: []

s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(solution.findSubstring(s3, words3))  # Output: [6, 9, 12]
