class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(k) -> bool:
            time = 0
            for p in piles:
                time += -(-p // k)
            
            return time <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

        