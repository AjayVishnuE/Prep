#  . 19 - 09 - 2023 
#  . 287. Find the Duplicate Number

# ... SOLUTION ...

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
                
        return low  

#  . 20 - 09 - 2023 
#  . 

# ... SOLUTION ...



#  . 

# ... SOLUTION ...

#  . 

# ... SOLUTION ...
#  . 

# ... SOLUTION ...

#  . 

# ... SOLUTION ...
