class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        option1 = max_index + 1
        option2 = n - min_index
        option3 = min_index + 1 + n - max_index

        return min(option1, option2, option3)