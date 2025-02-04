from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_logs = []
        num_logs = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                num_logs.append(log)
            else:
                str_logs.append((rest, identifier))

        str_logs.sort()
        sorted_str_logs = [f"{identifier} {rest}" for rest, identifier in str_logs]

        return sorted_str_logs + num_logs
