class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = []
        merged_arr = nums1 + nums2
        for i in range (1,len(merged_arr)):
            key = merged_arr[i]
            j = i-1

            while j >= 0 and merged_arr[j] > key:
                merged_arr[j+1] = merged_arr[j]
                j -= 1
            merged_arr[j+1] = key

        if len(merged_arr)%2 == 0:
            k = len(merged_arr)//2
            p = (merged_arr[k-1] + merged_arr[k])/2
            return p

        elif len(merged_arr)%2!= 0:
            c = len(merged_arr)//2
            return merged_arr[c] 