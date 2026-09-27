class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums_2_pointer = n - 1
        left_pointer = m - 1
        right_pointer = n + m - 1

        while nums_2_pointer >= 0 and left_pointer >= 0:
            print(left_pointer, right_pointer, nums_2_pointer)
            if nums2[nums_2_pointer] > nums1[left_pointer]:
                nums1[right_pointer] = nums2[nums_2_pointer]
                nums_2_pointer -= 1
            else:
                nums1[right_pointer] = nums1[left_pointer]
                left_pointer -= 1
            right_pointer -= 1
            
        while nums_2_pointer >= 0:
            nums1[right_pointer] = nums2[nums_2_pointer] 
            nums_2_pointer -= 1
            right_pointer -= 1 
        
        
            



        