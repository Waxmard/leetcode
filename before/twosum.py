from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {nums[0]: 0} # {val: index}
    for i in range(1, len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i

print(twoSum([2,7,11,15], 9))
