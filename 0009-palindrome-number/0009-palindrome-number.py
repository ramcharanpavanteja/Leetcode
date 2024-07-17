class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        return False