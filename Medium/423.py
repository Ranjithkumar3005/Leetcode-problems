class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        uniq = ["z", "w", "u", "x", "g"]
        num = []
        z = s.count("z")  # zero
        w = s.count("w")  # two
        u = s.count("u")  # four
        f = s.count("f") - u  # five
        x = s.count("x")  # six
        v = s.count("v") - f  # seven
        g = s.count("g")  # eight
        r = s.count("r") - z - u  # three
        o = s.count("o") - z - w - u  # one
        n = int((s.count("n") - v - o) // 2)
        return (
            "0" * z
            + "1" * o
            + "2" * w
            + "3" * r
            + "4" * u
            + "5" * f
            + "6" * x
            + "7" * v
            + "8" * g
            + "9" * n
        )
