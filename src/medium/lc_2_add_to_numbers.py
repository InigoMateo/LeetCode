"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        first_number = 0
        second_number = 0

        reverse_multiplier_first_number = 1
        while l1:
            first_number += reverse_multiplier_first_number * l1.val
            l1 = l1.next
            reverse_multiplier_first_number *= 10

        reverse_multiplier_second_number = 1
        while l2:
            second_number += reverse_multiplier_second_number * l2.val
            l2 = l2.next
            reverse_multiplier_second_number *= 10

        sum = first_number + second_number
        
        reversed_sum = 0
        while sum > 0:
            reversed_sum = reversed_sum * 10 + sum % 10
            sum = sum // 10

        # Handle the case where the sum is 0
        if reversed_sum == 0:
            return ListNode(0)

        first = True
        while reversed_sum > 0:
            num = reversed_sum % 10
            if first:
                head = ListNode(num, None)
                first = False
            else:
                new_node = ListNode(num, head)
                head = new_node
            reversed_sum = reversed_sum // 10

        return(head)
    
    def are_linked_list_equal(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return l1 is None and l2 is None

class TestAddToNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        solution_instance = Solution()

        ll1 = ListNode(2,ListNode(4,ListNode(3, None)))
        ll2 = ListNode(5,ListNode(6,ListNode(4, None)))
        expected_ll = ListNode(7,ListNode(0,ListNode(8, None)))

        result_ll = solution_instance.add_two_numbers(ll1, ll2)

        self.assertTrue(solution_instance.are_linked_list_equal(result_ll,expected_ll))

unittest.main()