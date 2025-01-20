class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        c = queryIP.count(".")
        if c == 0:
            c1 = queryIP.count(":")
            if c1 == 7:
                dum1 = queryIP.split(":")
                for i in dum1:
                    if len(i) > 4 or len(i) == 0:
                        return "Neither"
                    for j in i:
                        if j.isalpha() and (
                            (ord(j) > 70 and ord(j) < 91)
                            or (ord(j) > 102 and ord(j) < 123)
                        ):
                            return "Neither"
                return "IPv6"
            else:
                return "Neither"
        elif c == 3:
            if "-" in queryIP:
                return "Neither"
            dum = queryIP.split(".")
            for i in dum:
                if len(i) == 0:
                    return "Neither"
                for j in i:
                    if j.isalpha():
                        return "Neither"
                if int(i) > 255 or int(i) < 0 or (len(i) >= 2 and i[0] == "0"):
                    return "Neither"
            return "IPv4"
        else:
            return "Neither"
