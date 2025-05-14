"""
217.Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
import unittest

class Solution:
    def contains_duplicate_brute_force(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True   
        return False
    
    def contains_duplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for i in range(len(nums)):
            if nums[i] in count_dict:
                return True
            else:
                count_dict[nums[i]] = nums[i]
        return False
    
solution_instance = Solution()
    
class TestContainsDuplicate (unittest.TestCase):
    def test_contains_duplicate_brute_force(self):
        self.assertEqual(solution_instance.contains_duplicate_brute_force([1,2,3,1]), True)
    def test_contains_duplicate(self):
        self.assertEqual(solution_instance.contains_duplicate([1,2,3,1]), True)

unittest.main()
        