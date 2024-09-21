class Solution:
    # What we know
    # m ints in nums1 and n ints in nums2
    # each int is greater than the int before

    # Pseudocode
    # Index through each in in nums1 while comparing them to nums 2
    # for loops
    # If nums1[0] <= nums2[0] check nums1[1] vs nums2[0]
    # If nums1[1] >= nums2[0] add nums2[0] in the index 1 spot
    # i++, break cycle
    # continue until all are added

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # received syntax error for add "int"/"var" when 
        # declaring the variable (python doesn't require the type indicators)
        testNumber = 0
        arrLen = m + n
        # use 'and' instead of '&&'
        if m>0 and n>0:
          for num in nums1:
            index = nums1.index(num)
            if num == 0:
                nums1.remove(num)
            if (index+1) < m:
                if num < nums2[testNumber]:
                    continue
                else:
                    nums1.insert(index, nums2[testNumber])
                    nums2.pop(testNumber)
            else:
                nums1.extend(nums2)
        elif m==0 and n>0:
            nums1.extend(nums2)
        
        
        # RESULT RECEIVED
      # MEMORY LIMIT EXCEEDED
