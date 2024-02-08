class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Solusion 1- not passing the test case in Leetcode Consule but passing same tests on VSCode
        #temp_nums1 = nums1[:m]
        #temp_nums1.extend(nums2)
        #temp_nums1 = sorted(temp_nums1)
        #nums1 = temp_nums1
        
        # Set the last index of nums1 and nums2
        last = m + n - 1
    
    # Start from the end of nums1 and nums2
        while m > 0 and n > 0:
            # If the current element in nums1 is greater than in nums2, set it at the last position
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # Fill nums1 with leftover nums2 elements if any
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
            
                






        