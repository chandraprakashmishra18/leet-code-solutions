class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Track 3 largest numbers
        max1 = max2 = max3 = float('-inf')
        # Track 2 smallest numbers
        min1 = min2 = float('inf')
        
        for n in nums:
            # Update maximums
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
                
            # Update minimums
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
                
        # Compare the two possible maximum products
        return max(max1 * max2 * max3, min1 * min2 * max1)