#Author: Zach Naymik
#Date: March 5, 2022

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        rev_x = [0] * len(str_x)
        i = len(str_x) - 1
        j = 0
        while (i >= 0):
            rev_x[j] = str_x[i]
            i -= 1
            j += 1
        rev_x = ''.join(rev_x)
        if rev_x == str_x:
            return True
        else:
            return False
        