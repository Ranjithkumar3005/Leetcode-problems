class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        val1 = version1.split(".")
        val2 = version2.split(".")
        
        max_length = max(len(val1), len(val2))
        
        val1.extend(["0"] * (max_length - len(val1)))
        val2.extend(["0"] * (max_length - len(val2)))
        
        for i in range(max_length):
            if int(val1[i]) < int(val2[i]):
                return -1
            if int(val1[i]) > int(val2[i]):
                return 1
        
        return 0
