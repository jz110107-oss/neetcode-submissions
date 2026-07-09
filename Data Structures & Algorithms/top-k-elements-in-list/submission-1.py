class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_list = (Counter(nums).most_common())[0:k]
        return [item[0] for item in my_list]

        