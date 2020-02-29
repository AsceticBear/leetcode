'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
'''

from typing import List
from collections import Counter
from math import gcd

class Solution:
    # solution 1
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        print('count = ', count)

        key_min = min(count.keys(), key = (lambda k: count[k]))
        count_min = count[key_min] + 1
        # print('min count = ', count[key_min])
        
        for i in range(2, count_min):
            if all(v % i == 0 for v in count.values()):
                return True  
        
        return False
    
    # soluction 2
    def hasGroupsSizeX1(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values) >= 2


if __name__ == '__main__':
    s = Solution()

    deck1 = [1,2,3,4,4,3,2,1];
    assert s.hasGroupsSizeX(deck1) == True
    deck2 = [1]
    assert s.hasGroupsSizeX(deck2) == False
    deck3 = [1,1,1,2,2,2,3,3]
    assert s.hasGroupsSizeX(deck3) == False
    deck4 = [1,1]
    assert s.hasGroupsSizeX(deck4) == True
    deck5 = [1,1,2,2,2,2]
    assert s.hasGroupsSizeX(deck5) == True
    deck6 = [1,1,1,1,2,2,2,2,2,2]
    assert s.hasGroupsSizeX(deck6) == True