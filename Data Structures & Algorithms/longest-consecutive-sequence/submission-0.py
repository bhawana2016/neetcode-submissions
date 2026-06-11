class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The solution also gives the exact sequence
        set_nums = set(nums)
        longest = 0
        d = collections.defaultdict(list)
        for i in set_nums:
            if i-1 not in set_nums:
                length = 0
                while (i + length) in set_nums:
                    length += 1
                    d[i].append(i + length)
                longest = max(longest,length)

        return longest

        