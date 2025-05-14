"""
9. Palindrome Number 

Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reverseNumber = 0
            original = x

            while x > 0:
                reverseNumber = reverseNumber * 10 + x % 10
                x //=10

            if reverseNumber == original:
                return True
            else:
                return False
            
    def isPalindromeSimplified(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverseNumber, original = 0, x
        while x > 0:
            reverseNumber = reverseNumber * 10 + x % 10
            x //= 10
        
        return reverseNumber == original
    
    def isPalindromeHalfReverse (self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        
        reversed = 0
        temp = x
        while reversed < temp:

            reversed = reversed * 10 + temp % 10
            temp //= 10

        return reversed == temp or reversed // 10 == temp
    
ispalindrome = Solution()

class TestIsPalindrome (unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(ispalindrome.isPalindrome(121), True)
        self.assertEqual(ispalindrome.isPalindrome(-121), False)
        self.assertEqual(ispalindrome.isPalindrome(10), False)
    def test_isPalindromeSimplified(self):
        self.assertEqual(ispalindrome.isPalindromeSimplified(121), True)
        self.assertEqual(ispalindrome.isPalindromeSimplified(-121), False)
        self.assertEqual(ispalindrome.isPalindromeSimplified(10), False)
    def test_isPalindromeHalfReverse(self):
        self.assertEqual(ispalindrome.isPalindromeHalfReverse(121), True)
        self.assertEqual(ispalindrome.isPalindromeHalfReverse(-121), False)
        self.assertEqual(ispalindrome.isPalindromeHalfReverse(10), False)

if __name__ == "__main__":
    unittest.main()
