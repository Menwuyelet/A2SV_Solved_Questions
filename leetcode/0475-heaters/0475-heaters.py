class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # Find the insertion point where a house would fit in sorted heaters
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the heater on the right (if it exists)
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            # Distance to the heater on the left (if it exists)
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # The house will be covered by the closer of the two heaters
            closest_heater= min(dist_left, dist_right)
            
            # The global radius must be large enough to cover the worst-case house
            max_radius = max(max_radius, closest_heater)
            
        return max_radius