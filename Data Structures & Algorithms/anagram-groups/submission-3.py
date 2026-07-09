class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in range(len(strs)):
            ans[tuple(sorted(Counter(strs[i]).items()))].append(strs[i])
        return list(ans.values())