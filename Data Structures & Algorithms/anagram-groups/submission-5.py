class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        newstrs = defaultdict(list)

        for string in strs:
            newstrs[tuple(sorted(Counter(string).items()))].append(string)
        
        return list(newstrs.values())