"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List
import unittest


class Solution():
    def max_sub_array(self, nums: List[int]) -> int:

        n = len(nums)
        max_sub_array = -154
        acc_sub_array = 0
        
        for i in range(n):
            
            acc_sub_array = nums[i]   
        
            for i in range(i, n-1):
                if max_sub_array >= acc_sub_array + nums[i+1]:
                    break
                elif acc_sub_array < 0 and max_sub_array < 0:
                    max_sub_array = acc_sub_array
                    break
                else:
                    acc_sub_array = acc_sub_array + nums[i+1]

            max_sub_array = acc_sub_array if acc_sub_array > max_sub_array else max_sub_array

        return max_sub_array
    
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum
    
    def maxSubArrayClear(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
        
solution_instance = Solution()
                
class TestMaxSubArray(unittest.TestCase):
    def test_max_sub_array(self):
        self.assertEqual(solution_instance.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]),6)
        self.assertEqual(solution_instance.max_sub_array([-1,-2,-1,-4]),-1)
    def tes_maxSubArray(self):
        self.assertEqual(solution_instance.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
        self.assertEqual(solution_instance.maxSubArray([-1,-2,-1,-4]),-1)

if __name__ == "__main__":
    unittest.main()









