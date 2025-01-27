class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_map = {
            "0": "0",
            "1": "1",
            "8": "8",
            "5": "2",
            "2": "5",
            "6": "9",
            "9": "6",
        }
        invalid_digits = {"3", "4", "7"}

        good_count = 0

        for i in range(1, n + 1):
            ch = str(i)
            rotated = ""
            check = False

            for j in ch:
                if j in invalid_digits:
                    check = False
                    break
                if j in valid_map:
                    rotated += valid_map[j]
                    if valid_map[j] != j:
                        check = True

            if check:
                good_count += 1

        return good_count
