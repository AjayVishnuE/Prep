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
    

#  6. Zigzag Conversion

# ... SOLUTION ...

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        row_arr = [""] * numRows
        row_idx = 1
        going_up = True

        for ch in s:
            row_arr[row_idx-1] += ch
            if row_idx == numRows:
                going_up = False
            elif row_idx == 1:
                going_up = True
            
            if going_up:
                row_idx += 1
            else:
                row_idx -= 1
        
        return "".join(row_arr)
    

#  7. 

# ... SOLUTION ...



#  8. 

# ... SOLUTION ...



#  9. Palindrome Number

# ... SOLUTION ...

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        rev=0
        while(n>0):
            temp=n%10
            rev = rev*10 + temp
            n = n//10
        
        if(rev==x):
            return True
        else:
            return False
        
        # x =str(x)
        # if(x==x[::-1]):
        #     return True
        # else:
        #     return False
        

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

#  12. Integer To Roman

# ... SOLUTION ...

class Solution:
    def intToRoman(self, num: int) -> str:
        s=""
        dict1={
            1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M", 4 : "IV", 9 : "IX", 40 : "XL", 90 : "XC", 400 : "CD", 900 : "CM", 
        }
        l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for n in l:
            while n <= num:
                s += dict1[n]
                num-=n
        return s


#  13. Roman To Integer

# ... SOLUTION ...

class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1, "IV":4, "IX":9 , "XL":40 , "XC":90 , "CD":400 , "CM": 900, }
        val=0
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        for ele in s:
            val=val+dict1[ele]
        return val
    

#  14. Longest Common Prefix

# ... SOLUTION ...

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        n = min(strs, key=len)
        n = len(n)
        for i in range(n):
            x = strs[0]
            x = x[i]
            count=0
            for j in strs:
                if(j[i]==x):
                    count+=1
            if(count==len(strs)):
                s+=x
            else:
                return s
        else:
            return s


#  15. 

# ... SOLUTION ...





#  16. 

# ... SOLUTION ...




#  17. 

# ... SOLUTION ...




#  18. 

# ... SOLUTION ...




#  19. 

# ... SOLUTION ...




#  20. 

# ... SOLUTION ...




#  21. 

# ... SOLUTION ...




#  22. 

# ... SOLUTION ...




#  23. 

# ... SOLUTION ...




#  24. 

# ... SOLUTION ...





#  25. 

# ... SOLUTION ...




#  26. 

# ... SOLUTION ...





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
    

#  28. 

# ... SOLUTION ...




#  29. 

# ... SOLUTION ...




#  30. 

# ... SOLUTION ...




#  31. 

# ... SOLUTION ...




#  32. 

# ... SOLUTION ...




#  33. 

# ... SOLUTION ...






#  34. 

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




