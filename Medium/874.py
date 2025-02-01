class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacle_set = set(
            map(tuple, obstacles)
        )  # Convert obstacles to set of tuples for faster lookup
        print(obstacle_set)
        max1 = 0
        first = [0, 0]
        c = 0
        dir = ["north", "east", "south", "west"]

        for i in range(len(commands)):
            if commands[i] < 0:
                if commands[i] == -1:
                    c = (c + 1) % 4  # Turn right, ensure c is within [0, 3]
                else:
                    c = (c - 1 + 4) % 4  # Turn left, ensure c is within [0, 3]
            else:
                if dir[c] == "north":
                    for j in range(1, commands[i] + 1):
                        first[1] += 1
                        if tuple(first) in obstacle_set:
                            first[1] -= 1  # Step back if obstacle encountered
                            break
                elif dir[c] == "east":
                    for j in range(1, commands[i] + 1):
                        first[0] += 1
                        if tuple(first) in obstacle_set:
                            first[0] -= 1  # Step back if obstacle encountered
                            break
                elif dir[c] == "south":
                    for j in range(1, commands[i] + 1):
                        first[1] -= 1
                        if tuple(first) in obstacle_set:
                            first[1] += 1  # Step back if obstacle encountered
                            break
                elif dir[c] == "west":
                    for j in range(1, commands[i] + 1):
                        first[0] -= 1
                        if tuple(first) in obstacle_set:
                            first[0] += 1  # Step back if obstacle encountered
                            break
            max1 = max(max1, (first[0] ** 2 + first[1] ** 2))

        return max1
