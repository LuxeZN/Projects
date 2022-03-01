#Author: Zach Naymik!
#Date: February 28, 2022

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_total = 0
        for i in accounts:
            total = 0
            for j in i:
                total += j
            if (total > max_total):
                max_total = total
        return max_total
            
        
        