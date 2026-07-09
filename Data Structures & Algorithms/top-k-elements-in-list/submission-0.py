class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = sorted(list(tuple(Counter(nums).items())), key=lambda x: x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(count[i][0])
        return ans