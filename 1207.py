class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter

        count = Counter(arr)

        return len(count.values()) == len(set(count.values()))