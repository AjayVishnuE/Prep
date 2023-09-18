#  4. Medaian of Two Sorted Arrays 

# ... SOLUTION ...

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        s = 0
        for j in range(n):
            nums1.append(nums2[j])
        l=len(nums1)
        nums1 = sorted(nums1)
        if (l % 2 == 0):
          s = nums1[(l//2) - 1]+nums1[(l//2)]
          s = s/2
        else:
          s = nums1[((l-1)//2)]
        return s
    

#  11. Container With Most Water

# ... SOLUTION ...

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxval=0
        l = 0 
        r = len(height) -1 
        while l <= r:
            length = r - l
            h = min(height[l], height[r])
            if(maxval < length * h):
                maxval = length*h
            if(height[l] <= height[r]):
                l+=1
            else:
                r-=1
        return maxval


#  27. Remove Element 

# ... SOLUTION ...

#  . 

# ... SOLUTION ...

#  . 

# ... SOLUTION ...

