class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips.length <= 1000
        stops = [0] * 1001
        for t in trips:
            stops[t[1]] += t[0] # people increase
            stops[t[2]] -= t[0] # people decrease
        for ppl in stops:
            capacity -= ppl
            if capacity < 0:
                return False
        return True