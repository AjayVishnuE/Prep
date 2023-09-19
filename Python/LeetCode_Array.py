#  1. Two Sum 

# ... SOLUTION ...

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=len(nums)
        for i in range(x):
            for j in range(i+1,x):
                if(nums[i]+nums[j]==target):
                    return [i,j]
                
#  2. 

# ... SOLUTION ...



#  3. Longest Substring Without Repeating Characters

# ... SOLUTION ...

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x, count = 0, 0
        l = []
        for i in range(len(s)):
            while s[i] in l:
                l.remove(s[x])
                x += 1
                
            l.append(s[i])
            count = max(count, (i - x + 1))
        
        return count
    

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
    

#  5. Longest Palindromic Substring

# ... SOLUTION ...

class Solution:
    def longestPalindrome(self, s: str) -> str:
        t,ans="",""
        size=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                t+=s[j]
                if t==t[::-1] and len(t)>size:
                    ans=t
                    size=len(t)
            t=""
        return ans
    

#  6. 

# ... SOLUTION ...



#  7. 

# ... SOLUTION ...



#  8. 

# ... SOLUTION ...



#  9. 

# ... SOLUTION ...



#  10. 

# ... SOLUTION ...



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

class Solution(object):
    def removeElement(self, nums, val):
        length = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1

        return length
    

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




