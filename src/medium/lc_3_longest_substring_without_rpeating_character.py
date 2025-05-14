"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
import unittest

class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        n = len(s)
        substring = {}
        substring_length = 0
        max_substring_length = 0

        for i in range(n):
            if substring.get(s[i], False):
                substring = {}
                substring[s[i]] = 1
                substring_length = 1
                max_substring_length = max_substring_length if substring_length < max_substring_length else substring_length
            else:
                substring[s[i]] = 1
                substring_length += 1
                max_substring_length = max_substring_length if substring_length < max_substring_length else substring_length
        
        return max_substring_length
             
solution_instance = Solution()

class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_length_of_longest_substring(self):
        self.assertEqual(solution_instance.length_of_longest_substring('"dvdf"'),2)

unittest.main()