"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

nums = [1,2,3]
print(nums[2])
for i in range(len(nums)):
    print(i)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]]=i

        for value, key in nums_map.items():
            addend1 = value
            addend1_index = key
            addend2 = target - addend1
            addend2_index = nums_map[addend2]
        return (addend1_index, addend2_index)
    
if __name__ == "__main__":
    solution = Solution
    solution_values= solution.twoSum([1,2,3],3)
    print(solution_values)
