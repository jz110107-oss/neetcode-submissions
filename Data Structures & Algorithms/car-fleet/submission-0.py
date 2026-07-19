class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = [(0,0)] * len(position)
        fleet, currenttime, highesttime = 0, 0, 0

        for i in range(len(position)):
            time[i] = (position[i], (target-position[i])/speed[i])
        
        time.sort()

        while time:
            currenttime = time.pop()[1]
            if currenttime > highesttime:
                highesttime = currenttime
                fleet += 1
        return fleet