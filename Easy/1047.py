class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(0, len(s)):
            if stack != [] and stack[len(stack) - 1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        strs = ""
        for i in stack:
            strs += i
        return strs
