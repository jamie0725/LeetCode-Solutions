"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


""" 


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: 
            count = 1
        else:
            count = 10
            for iTime in range(2,n+1):
                sNum = 9
                temp = iTime
                sProduct = 1
                counter = 2
                while temp > 0:
                    sProduct *= sNum
                    counter -= 1
                    if counter <= 0:
                        sNum -= 1
                    temp -= 1
                count += sProduct
        return count
