class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.ans = set()
        used = [False] * len(tiles)

        def backtrack(arr):
            if arr:
                self.ans.add(arr)
            for i in range(len(tiles)):
                if not used[i]:
                    used[i] = True
                    backtrack(arr + tiles[i])
                    used[i] = False

        backtrack("")
        return len(self.ans)
