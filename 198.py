class Solution:
    def rob(self, nums: list[int]) -> int:
        prev1 = 0  # Max profit up to house i - 1
        prev2 = 0  # Max profit up to house i - 2
        
        for num in nums:
            # Decide whether to rob current house + prev2 or keep prev1
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1