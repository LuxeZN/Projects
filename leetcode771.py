#Author: Zach Naymik
#Date: March 5, 2022

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        i = 0 
        while (i < len(jewels)):
            for j in stones:
                if (jewels[i] == j):
                    count += 1
            i += 1
        return count