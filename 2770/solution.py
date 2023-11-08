from typing import List

from leetcode_imports import *


def maximumJumps(nums: List[int], target: int) -> int:
    n = len(nums)
    dp = [-1] * n  # at this point all -1s means all indexes unreachable
    dp[0] = 0  # (index, max jumps)

    for i in range(1, n):  # iterate forward through nums
        for j in range(i):  # iterate up to point in nums
            if (
                abs(nums[i] - nums[j]) <= target
            ):  # comparison of jump from 2 diff spots, i and j
                dp[i] = max(
                    dp[i], dp[j] + 1
                )  # if using the new jump is higher, use that, otherwise keep max jumps
    return dp[-1]  # returns -1 since that's how it was initialized


run(maximumJumps([0, 2, 1, 3], 1), -1)
run(maximumJumps([1, 2, 1], 0), 1)
run(maximumJumps([1, 2, 3, 0], 1), 1)
run(maximumJumps([1, 0, 2], 1), 1)
run(maximumJumps([0, 1], 0), -1)
run(maximumJumps([1, 3, 4, 0, 2], 2), 3)
