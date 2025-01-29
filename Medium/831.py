class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = ""
        if "@" in s:
            s = s.lower()
            strs = s[0] + "*****" + s[s.index("@") - 1] + s[s.index("@") : len(s)]
        else:
            dum = ""
            for i in s:
                print(i)
                if i.isdigit():
                    dum += i
            print(dum)
            if len(dum) == 10:
                strs = "***-***-" + dum[6:11]
            elif len(dum) == 11:
                strs = "+*-***-***-" + dum[7:12]
            elif len(dum) == 12:
                strs = "+**-***-***-" + dum[8:13]
            else:
                strs = "+***-***-***-" + dum[9:14]
        return strs
