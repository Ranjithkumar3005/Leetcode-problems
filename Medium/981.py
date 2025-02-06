import bisect


class TimeMap:

    def __init__(self):
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.h:
            self.h[key].append((timestamp, value))
        else:
            self.h[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h:
            return ""
        values = self.h[key]

        i = bisect.bisect_right(values, (timestamp, chr(127))) - 1

        if i >= 0:
            return values[i][1]
        return ""


# Example usage:
# obj = TimeMap()
# obj.set("foo", "bar", 1)
# param_2 = obj.get("foo", 1)  # Should return "bar"
# param_2 = obj.get("foo", 3)  # Should return "bar" because it's the latest value before or at timestamp 3
