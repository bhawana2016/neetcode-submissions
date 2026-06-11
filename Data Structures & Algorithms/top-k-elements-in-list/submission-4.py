class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        print(d)
        result_d = {x:y for x,y in list(sorted(d.items(), key=lambda x:x[1], reverse=True))}
        result_l = list(result_d.keys())
        return result_l[:k]