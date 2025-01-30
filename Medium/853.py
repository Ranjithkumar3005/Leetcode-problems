from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        fleets = 0
        time_to_target = -1

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > time_to_target:
                fleets += 1
                time_to_target = time

        return fleets
