class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i in strs:
            sorted_str = "".join(sorted(i))
            d[sorted_str].append(i)
        #print(d)
        #l_out = []
        # Creates the grouped lists directly
        result_lists = list(d.values())
        print(result_lists)
        return result_lists