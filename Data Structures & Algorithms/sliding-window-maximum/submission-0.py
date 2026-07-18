class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        
        q = []
        ans = []

        for i in range(k):
            heapq.heappush(q, (-nums[i], i))

        while r < len(nums):
            while q[0][1] > r or q[0][1] < l:
                heapq.heappop(q)
            ans.append(-q[0][0])
            r += 1
            if r < len(nums):
                heapq.heappush(q, (-nums[r], r))
            
            l += 1
        return ans

