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
    '''One pass dict'''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in num_dict:
                return(num_dict[complement], i)
            num_dict[nums[i]] = i

        return [] #No solution found


class Sotuion_Two:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        n = len(nums)

        for i in range(n):
            num_dict[nums[i]]=i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in num_dict and i != num_dict[complement]:
                return (i, num_dict[complement])

        return [] #No solution found


if __name__ == "__main__":
    solution = Solution()
    solution_values= solution.twoSum([1,2,3],3)
    solution_values= solution.twoSum([1,2,3],3)
    print(solution_values)
