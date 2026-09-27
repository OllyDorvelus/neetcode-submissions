class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_ptr = n + m - 1
        n = n - 1
        m = m - 1
        
        while n >= 0 and m >= 0:
            if nums2[n] > nums1[m]:
                nums1[last_ptr] = nums2[n]
                n -= 1
            else:
                nums1[last_ptr] = nums1[m]
                m -= 1
            last_ptr -= 1
            
        while n >= 0:
            nums1[last_ptr] = nums2[n] 
            n -= 1
            last_ptr -= 1 
        
        
            



        