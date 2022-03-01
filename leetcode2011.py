#Author: Zach Naymik
#Date: February 28, 2022

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for i in operations:
            if (i == "++X" or i == "X++"):
                x += 1
            elif (i == "--X" or i == "X--"):
                x -= 1
        return x
        