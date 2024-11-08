class FirstWrongSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
           # Count instances of a value w/in array
         # if found two or more instances return true 
       # else return false *)
        for number in nums:
            count = nums.count(number)
            if count >= 2:
                return True
        
        return False

#   Received an exceeded time limit error.
#   During interview ask:
#   - is there a limit to the amount of values in the array being tested

# NOTES:
# Time complexity is O(n^2)
# This is b/c count() fcn iterates through the array again to find the number of counts of a value [count() has a time complexity of O(n)

# It is inefficient to use a fcn with time complexity of O(n^2) if the input list nums has a large size (e.g., n = 10^5 or more)



class CorrectSolutionSorting:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1: sort and compare 
        nums.sort() # this sorts the list into asc. order

        # go through list and compare number to previous number
        # if they are equal return true if not continue 

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False

        # complexity of O(n) 


class CorrectSolutionSet:
    # a set() is an unordered collection of unique elements that allows for no duplicates to be included
    # if you try to add a duplicate value it will be ignored
    # ex goodSet = { 1, 2, 3, 4 } vs. notGoodSet = { 1, 1, 2, 3}
