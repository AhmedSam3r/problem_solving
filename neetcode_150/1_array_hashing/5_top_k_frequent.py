import heapq
from collections import Counter


def topKFrequent(nums, k):
    '''
    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(n) for storing the count dictionary and sorted list.
    '''
    # counter = Counter(nums)
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    # this approach doesn't work
    # counter = {num: counter.get(num, 0) + 1 for num in nums}
    sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Get the top k elements
    return [item[0] for item in sorted_items[:k]]


def topKFrequent_bucket_sort(nums, k):
    '''

    it's a bucketsort not count sort
        since we take each index and put a list inside it, then we iterate over each bucket and order them to get their values # NOQA 501
        each index has range of values (list of elements repeated)
    bucket sort expalanation
        https://www.youtube.com/watch?v=VuXbEb5ywrU
    count sort expalanation
        https://youtu.be/pEJiGC-ObQE?list=PLjuNEWpkTZauDAstircLx0B-tsERPsjtT
    space complexity:
        O(n)
    time complexity:
        O(n) + O(n) => O(n)
    notes:
        `freq = [[]] * (len(nums)+1)`
            so important to add +1, to consider the array as if it's 1-indexed based
            example: [1] "1" should be assigned to 1st index [[], [1]]

        `freq[count] = freq[count] + [value]`
            If we append it directly, since initially all the indexes refers to the same empty list address
            All indexes will be changed as they point to the same memory address

    '''
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    freq = [[]] * (len(nums)+1)
    for value, count in counter.items():
        freq[count] = freq[count] + [value]
    result = []    
    print("FREQ ==>", freq, len(freq))
    for i in range(len(freq)-1, 0, -1):
        lst = freq[i]
        if not lst:
            continue
        while lst and len(result) < k:
            result.append(lst.pop())
        if len(result) == k:
            break
    return result


def topKFrequent_heapq(nums, k):
    """
    time complexity:
        O(nlogk), it's different from nxlogn as we can assume k < n 
            log(k) for pushing/popping (inserting/removing) an item
    space complexity:
        O(n)
    note:
        by default heapq is a min heap 
        using the min heap property since we always pop if heap > k,
            we're making sure that we always have the greatest elements on our heap aka most frequent
        check this link:
            https://youtu.be/phNDYf1xzco?t=263
    """

    counter = Counter(nums)
    heap = []
    print("counter ==>", counter)
    for num, count in counter.items():
        print(f"num={num}, count={count}")
        if len(heap) < k:
            print("<<<<<<<<<<<<<<<<<<<<<")
            heapq.heappush(heap, (count, num))  # we want to sort by count

        else:
            print("------------exceeded k-------")
            # push an item, then pop the smallest, so we always keep the greatest items inside the heap
            # mmmmmm interesting

            smallest = heapq.heappushpop(heap, (count, num))
            print(f"smallest {smallest}")
        print("heap ==>", heap)
    return [num for count, num in heap]

class MaxHeap:
    def heapify(self, arr, size, index):
        left = (2 * index) + 1
        right = (2 * index) + 2
        smallest = index
        if left < size and arr[left] > arr[smallest]:
            smallest = left
        if right < size and arr[right] > arr[smallest]:
            smallest = right

        if smallest != index:
            arr[index], arr[smallest] = arr[smallest], arr[index]
            self.heapify(arr, size, smallest)

    def heapsort(self, arr):
        n = len(arr)

        # Build max heap
        for i in range((n//2 - 1), -1, -1):
            self.heapify(arr, n, i)
        for n in range(n-1, 0, -1):
            arr[0], arr[n] = arr[n], arr[0]
            self.heapify(arr, n, 0)
        return arr


def topKfrequent_heap_sort(nums, k):
    """
    time complexity:
        O(nlogk), it's different from nxlogn as we can assume k < n
    space complexity:
        O(n)
    """
    obj = MaxHeap()
    arr = obj.heapsort(nums)
    print("arr ==>", arr)
    most_freq = set()
    most_freq.add(arr[0])
    found = 1
    for i in range(1, len(arr)):
        if found == k:
            break
        most_freq.add(arr[i])
        if arr[i] != arr[i-1]:
            found += 1

    return list(most_freq)


nums = [3, 2, 2, 4, 4, 1, 1, 1]
k = 2
r = topKFrequent_bucket_sort(nums, k)
print("R ==>", r)

nums = [1]
k = 1
# r = topKFrequent_bucket_sort(nums, k)
# print("R ==>", r)
# r = topKfrequent_heap_sort(nums, k)
# print("R ==>", r)

nums = [3, 2, 2, 4, 4, 1, 1, 1, 5]
# nums = [3, 2, 2, 4, 4, 1, 1, 1, 5, 5, 5, 5]
k = 2
r = topKFrequent_heapq(nums, k)
print("R ==>", r)
