
# Brute Forec

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]


# Optimized


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        number = {}  # dictionary - hash map to store the number and their indices

        for i, num in enumerate(nums):
            if target - num in number:
                return [i, number[target-num]]

            number[num] = i

        return -1
