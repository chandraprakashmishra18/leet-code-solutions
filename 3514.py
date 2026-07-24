class Solution:
    def uniqueXorTriplets(self, nums):
        MAX_XOR = 2048  # nums[i] <= 1500, so XOR values are < 2048

        pair_xors = set()
        ans = set()

        n = len(nums)

        for j in range(n):
            for k in range(j, n):
                pair_xors.add(nums[j] ^ nums[k])

        for x in nums:
            for p in pair_xors:
                ans.add(x ^ p)

        return len(ans)