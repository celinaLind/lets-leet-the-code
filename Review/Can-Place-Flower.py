"""
Easy Problem

Description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

# Successful Solution - 13ms

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        freePlot = flowerbed[0]
        plots = 0
        lenBed = len(flowerbed)
        if n > lenBed:
            return False
        for i in range(lenBed):
            if freePlot == 0 and flowerbed[i] == 0:
                if i < lenBed-1:
                    if flowerbed[i+1] != 1:
                        plots += 1 
                        freePlot = 1
                else:
                    plots +=1
                    freePlot = 1
                print(i, plots)
            elif flowerbed[i] == 0:
                freePlot = flowerbed[i]
            elif flowerbed[i] == 1:
                freePlot = flowerbed[i]
        
        return plots >= n
    
# Better Solution - 0ms

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        leng = len(flowerbed)

        for i in range(leng):
            if(flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0 )and ( i == leng - 1 or flowerbed[i+ 1] == 0)):
                flowerbed[i] = 1
                count += 1
                i += 1
            if count >= n :
                 return True
        
        return False