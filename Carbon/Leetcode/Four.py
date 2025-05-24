# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
    
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        merged = []
        i, j = 0, 0
        total_arr_length = len(nums1) + len(nums2)

        # conditions for edge cases
        if total_arr_length == 0:
            return 0
        if total_arr_length == 1:
            return nums1[0] if len(nums1) == 1 else nums2[0]
        if total_arr_length == 2:
            if len(nums1) == 0:
                return float(nums2[0] + nums2[1]) / 2
            if len(nums2) == 0:
                return float(nums1[0] + nums1[1]) / 2
            else:
                return float(nums1[0] + nums2[0]) / 2

        # while the merged array is < half the total length of both arrays (position of the median) 
        while len(merged) < (total_arr_length // 2) + 1:
            if i < len(nums1) and (j == len(nums2) or nums1[i] <= nums2[j]):
                merged.append(nums1[i])
                i += 1
            elif j < len(nums2) and (i == len(nums1) or nums2[j] < nums1[i]):
                merged.append(nums2[j])
                j += 1

        #if the total length of both arrays are odd get last element in merged array
        if total_arr_length % 2 == 1: 
            return merged[-1]
        else:
            return float(merged[-2] + merged[-1]) / 2

        
main = __name__ == "__main__"
if main:
    solution = Solution()

    nums1 = [1,2]
    nums2 = [3,4]
    print(solution.findMedianSortedArrays(nums1, nums2)) 

    nums1 = [1, 1, 3, 4, 5, 9]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 3.5

    # Both arrays empty
    nums1 = []
    nums2 = []
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 0

    # One array empty, one small
    nums1 = []
    nums2 = [4]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 4

    # One array empty, one large
    nums1 = []
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 5.5

    # Both arrays size 1
    nums1 = [1]
    nums2 = [2]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 1.5

    # Both arrays size 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 2.5

    # Large arrays
    nums1 = list(range(0, 1000, 2))  # Even numbers 0-998
    nums2 = list(range(1, 1001, 2))  # Odd numbers 1-999
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 499.5

    # Arrays with negative numbers
    nums1 = [-5, -3, -1, 0]
    nums2 = [1, 2, 3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 0.5

    # Arrays with duplicates
    nums1 = [2, 2, 2]
    nums2 = [2, 2, 2]
    print(solution.findMedianSortedArrays(nums1, nums2))  # Expected: 2