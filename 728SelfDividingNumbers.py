"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for number in range(left, right + 1):
            temp = number
            for time in range(len(str(number))):
                if temp % 10 == 0:
                    break
                if number % (temp % 10) == 0:
                    temp /= 10
                else:
                    break
                if time == len(str(number)) - 1:
                    result.append(number)
        return result
