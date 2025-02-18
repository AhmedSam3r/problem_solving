class TimeMap:
    """
    time complexity (O(1 or N) + O(log(N)))
        - set an element + search array
    space complexity O(N)
    given this requirement `timestamp_prev <= timestamp`, the equal make it a search problem
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        # we can remove condition by adding `defaultdict(list)`
        if not (key in self.store):
            self.store[key] = []
        self.store[key].append(pair)

    def binary_search(self, timestamps, target: int) -> int:
        """
        some solving it `if target > timestamp_prev:` and `left<=right` return timestamps[right] if right >= 0
        """
        left, right = 0, len(timestamps) - 1
        while left < right:
            mid = (left+right) // 2
            timestamp_prev = timestamps[mid][0]
            if target > timestamp_prev:
                left = mid + 1
            else:
                right = mid
        # to solve [10, 20] list and target=15, so we can return 10, not 20
        # this made the solution work to get the lower bounds
        return (timestamps[right]
                if timestamps[right][0] <= target
                else timestamps[right-1])

    def get_brute(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        seen = 0

        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.keyStore[key][seen][-1]

    def get(self, key: str, timestamp: int) -> str:
        """using binary search"""
        print(self.store)
        if not (key in self.store):
            return ""
        ts, v = self.binary_search(self.store[key], timestamp)
        print(f"ts={ts}, v={v}, searchTS={timestamp}, cond={timestamp >= ts}")
        return v if timestamp >= ts else ""


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
res = timeMap.get("foo", 1)         # return "bar"
assert res == "bar"
res = timeMap.get("foo", 3)         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
assert res == "bar"
timeMap.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
res = timeMap.get("foo", 4)         # return "bar2"
assert res == "bar2"
res = timeMap.get("foo", 5)         # return "bar2"
assert res == "bar2"

res = timeMap.get("foo", 0)         # return "bar2"
assert res == ""

print("-------------------")
print("-------------------")
print("-------------------")
print("-------------------")
print("-------------------")

timeMap = TimeMap()
timeMap.set("love", "high", 10)
timeMap.set("love", "low", 20)

print('---------------')
res = timeMap.get("love", 5)
assert res == ""
res = timeMap.get("love", 10)
assert res == "high"
res = timeMap.get("love", 15)
assert res == "high"
res = timeMap.get("love", 20)
assert res == "low"
print("RES ==>", res)
res = timeMap.get("love", 25)
assert res == "low"
