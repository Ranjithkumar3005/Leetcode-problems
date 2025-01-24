class Solution:
    def maximumSwap(self, num: int) -> int:
        dum = []
        val = str(num)
        for i in val:
            dum.append(int(i))
        dum1 = sorted(dum, reverse=True)
        dum2 = dum[::-1]
        str1 = ""
        check = True
        for i in range(0, len(dum)):
            if dum[i] != dum1[i] and check:
                check = False
                inx = dum2.index(dum1[i])
                dum2[inx] = dum[i]
                dum = dum2[::-1]
                str1 += str(dum1[i])
            else:
                str1 += str(dum[i])
        return int(str1)
