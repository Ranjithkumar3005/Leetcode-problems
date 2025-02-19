class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        h = {
            0: 0,
            1: 31,
            2: 59,
            3: 90,
            4: 120,
            5: 151,
            6: 181,
            7: 212,
            8: 243,
            9: 273,
            10: 304,
            11: 334,
        }
        arr = date.split("-")
        year = int(arr[0])
        check = False
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            check = True
        mon = int(arr[1])
        days = h[mon - 1] + int(arr[2])
        if mon > 2 and check:
            return days + 1
        return days
