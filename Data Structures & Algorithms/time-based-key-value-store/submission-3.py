class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        array = self.timemap[key]
        if not array:
            return ""
        
        l, r = 0, len(array) - 1
        res = ""

        while l <= r:
            middle = (l + r)//2

            if array[middle][0] <= timestamp:
                res = array[middle][1]
                l = middle + 1
            else:
                r = middle - 1
            
        return res
        
