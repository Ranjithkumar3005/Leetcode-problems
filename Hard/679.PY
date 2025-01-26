from itertools import permutations, product


def judgePoint24(cards):
    def is_close(x, y):
        return abs(x - y) < 1e-6

    def evaluate(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:  # Avoid division by zero
                return float("inf")
            return a / b

    def backtrack(nums):
        if len(nums) == 1:  # Base case: only one number left
            return is_close(nums[0], 24)

        # Try every pair of numbers and every operator
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:  # Pick two different numbers
                    for op in ["+", "-", "*", "/"]:
                        # Create a new list excluding the chosen numbers
                        next_nums = [
                            nums[k] for k in range(len(nums)) if k != i and k != j
                        ]
                        # Add the result of the operation
                        next_nums.append(evaluate(nums[i], nums[j], op))
                        # Recurse
                        if backtrack(next_nums):
                            return True
        return False

    # Try all permutations of the cards
    for perm in permutations(cards):
        if backtrack(list(perm)):
            return True

    return False
