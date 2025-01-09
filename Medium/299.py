class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        h = {}

        for i in secret:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1

        cows = 0
        bulls = 0

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                h[guess[i]] -= 1

        for i in range(len(guess)):
            if secret[i] != guess[i] and guess[i] in h and h[guess[i]] > 0:
                cows += 1
                h[guess[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"
