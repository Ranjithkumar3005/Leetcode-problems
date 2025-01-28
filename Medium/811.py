class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dum = []
        h = {}

        for i in range(0, len(cpdomains)):
            values = cpdomains[i].split(" ")
            arr = values[1].split(".")
            if len(arr) == 2:
                sum = arr[0] + "." + arr[1]
                if sum in h:
                    h[sum] += int(values[0])
                else:
                    h[sum] = int(values[0])
                if arr[1] in h:
                    h[arr[1]] += int(values[0])
                else:
                    h[arr[1]] = int(values[0])
            else:
                sum = arr[0] + "." + arr[1] + "." + arr[2]
                if sum in h:
                    h[sum] += int(values[0])
                else:
                    h[sum] = int(values[0])
                sum = arr[1] + "." + arr[2]
                if sum in h:
                    h[sum] += int(values[0])
                else:
                    h[sum] = int(values[0])
                if arr[2] in h:
                    h[arr[2]] += int(values[0])
                else:
                    h[arr[2]] = int(values[0])

        for i in h:
            str1 = str(h[i]) + " " + i
            dum.append(str1)
        return dum
