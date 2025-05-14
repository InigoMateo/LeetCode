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
# The typing module provides support for type hints, which help you specify the expected types of variables of variables, function arguments and return variables
from typing import List, Tuple
import unittest

def addends_index_brute_force (nums: List [int], target: int) -> Tuple[int, int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return (i,j)
    return ()

def addends_index_two_pass_hash_table (nums: List[int], target: int) -> Tuple[int,int]:
    numMap = {}
    n = len(nums)
    for i in range(n):
        numMap[nums[i]] = i
    for i in range(n):
        addend2 = target - nums[i]
        if addend2 in numMap and numMap[addend2] != i:
            return (i, numMap[addend2])
        
def addends_index_one_pass_hash_table (nums: List[int], target: int) -> Tuple[int, int]:
    n = len(nums)
    numsMap = {}
    for i in range(n):
        addend2 = target - nums[i]
        if addend2 in numsMap:
            return (numsMap[addend2], i)
        else:
            numsMap[nums[i]] = i
    return()

class TestTwoSumFunction(unittest.TestCase):
    def test_addends_index_brute_force(self):
        self.assertEqual(addends_index_brute_force([2,7,11,15], 9),(0,1))
        self.assertEqual(addends_index_brute_force([3,2,4], 6),(1,2))
        self.assertEqual(addends_index_brute_force([3,3], 6),(0,1))
    
    def test_addends_index_two_pass_hash_table(self):
        self.assertEqual(addends_index_two_pass_hash_table([2,7,11,15], 9),(0,1))
        self.assertEqual(addends_index_two_pass_hash_table([3,2,4], 6),(1,2))
        self.assertEqual(addends_index_two_pass_hash_table([3,3], 6),(0,1))

    def test_addends_index_one_pass_hash_table(self):
        self.assertEqual(addends_index_one_pass_hash_table([2,7,11,15], 9),(0,1))
        self.assertEqual(addends_index_one_pass_hash_table([3,2,4], 6),(1,2))
        self.assertEqual(addends_index_one_pass_hash_table([3,3], 6),(0,1))

if __name__ == "__main__":
    unittest.main()

    # mylist = [1,2,3,4]
    # print(mylist)  
    # print(len(mylist))
    # print(mylist[0])
    # print(addends_index_brute_force(mylist,7))
    # print(addends_index_two_pass_hash_table(mylist, 7))
    # print(addends_index_one_pass_hash_table(mylist, 7))    

    # myHashMap = {3: 0, 4: 1, 2: 2, 1: 3}
    # print(myHashMap)
    # print(len(myHashMap))
    # print(f"{'Yes' if 2 in myHashMap else 'No'}" )
    # for key in myHashMap: print(key)
    # for value in myHashMap.values(): print(value)
    # for key, value in myHashMap.items(): print(key,value)
    # for i, j in enumerate(mylist): print(i,j)

    # add = lambda x, y: x + y
    # print(add(3,2))

    
