from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        '''Create an empty dictionary to store numbers from the input list. This allow O(1) complexity.'''
        for i, num in enumerate(nums):
            '''This loops over the input list nums, using the enumerate function'''
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    result = solution.twoSum(nums, target)
    print(f"Result: {result}")
