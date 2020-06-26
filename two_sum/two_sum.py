from typing import List
from collections import deque

def run(nums: List[int], target: int) -> List[int]:
    mums = deque(nums)
    mums = sorted(mums)
    for i in range(len(mums)-1):
        for j in range(i+1,len(mums)):
            if mums[j] == target-mums[i]:
                if nums.index(mums[i]) == nums.index(mums[j]):
                    tmp = nums.index(mums[i])
                    nums[nums.index(mums[i])] = (nums[nums.index(mums[j])]+1)
                    return [tmp,nums.index(mums[j])]
                return [nums.index(mums[i]),nums.index(mums[j])]
