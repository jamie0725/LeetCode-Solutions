"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        string = []
        for i in range(1,n+1):
            if(i % 15 == 0):
                string.append('FizzBuzz')
            elif(i % 5 == 0):
                string.append('Buzz')
            elif(i % 3 == 0):
                string.append('Fizz')
            else:
                string.append(str(i))
                
        return string
