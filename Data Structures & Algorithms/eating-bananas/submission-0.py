class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 0

        for pile in piles:
            r = max(r, pile)
        
        while l < r:
            middle = (l + r)//2

            if self.timetaken(middle, piles) > h:
                l = middle + 1
            else:
                r = middle
        
        return l
    
    def timetaken(self, rate, piles):
        total = 0
        for pile in piles:
            total += math.ceil(pile/rate)
        return total
