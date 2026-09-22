class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tMap:
            self.tMap[key].append((value, timestamp))
        else:
            self.tMap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tMap:
            return ""
        
        tKeyList = self.tMap[key]

        left = 0
        right = len(tKeyList) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if timestamp == tKeyList[mid][1]:
                return tKeyList[mid][0]

            if timestamp < tKeyList[mid][1]:
                right = mid - 1
            else:
                left = mid + 1

        if right < 0:
            return ""
    
        return tKeyList[right][0]
    