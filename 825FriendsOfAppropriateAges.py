"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?
"""

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        total = 0
        age = [0] * 120
        for i in range(len(age)):
            age[i] += ages.count(i+1)
                
                
                
        for i1, n1 in enumerate(age):
            for i2, n2 in enumerate(age):
                age1 = i1 + 1
                age2 = i2 + 1
                if (n1 != 0) & (n2 != 0):
                    if (age2 > 0.5 * age1 + 7) & (age2 <= age1) & (age2 <= 100 | age1 >= 100):
                        total += n1*n2
                        if(age1 == age2):
                            total -= n1
                        
                        
        
        return total
            
