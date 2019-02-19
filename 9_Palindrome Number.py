class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x=str(x)
        str_rev=str_x[::-1]
        if str_rev==str_x:
            return True
        return False
