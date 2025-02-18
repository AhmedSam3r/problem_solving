from collections import defaultdict, OrderedDict
from typing import Optional, Union



class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.val = val
        self.key = key
        self.prev = self.next = None

    def display(self):
        temp = self
        print("--------------DISPLAY-----------------------------")
        while temp:
            print(f"current={self.key}:{self.val}, address={id(temp)}")
            temp = temp.next
        print("--------------DISPLAY-----------------------------")

    def __str__(self):
        if self.val is not None:
            return str(self.val)
        return "EMPTY"


class LRUCacheLLV1:
    """

    notes:
        - not working but ...
        - the crux about this solution is trying to visualize the dummy note of
            left LRU and right MRU
        - the missing part was creating a prev node (thought of it)
            and adding dummy nodes for the DLL
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict()
        self.head = self.cur = Node(val=-1)

    def get(self, key: int) -> int:
        result = self.cache.get(key, None)
        print(f"key={key}:: result={result}, type={type(result)}")
        if result is not None:
            print(f"moving head to front ={self.head}")
            self.head.next = self.head.next.next
            # -1 -> 1 -> 2
            self.cur.next = result
            self.cur = self.cur.next
            self.cur.next = None
            # becomes -1 -> 2 -> 1 so 2 is the least recent used
            print(f"head={self.head.next}, result={result}, self.cur={self.cur}")
        return result.val if result else -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            print(f"self.head.next={self.head.next}")
            self.cache.pop(self.head.next.key)
            # -1 -> 2 -> 1
            self.head.next = self.head.next.next
        else:
            self.capacity -= 1
        print(f"PUT VALUE = {value},, self.cur={self.cur}")
        
        self.cur.next = Node(key=key, val=value)
        self.cache[key] = self.cur.next
        self.cur = self.cur.next
        print("END")


class LRUCacheLLV2:
    """
    notes:
        - the crux about this solution is trying to visualize the dummy note of
            left LRU and right MRU
        - finally worked, LL problems requires a lot of focus when assigning pointers
            and to update the methods accordingly
        - this solutions beats 42% in runtime and 88% in memory
            - ordered dict is more efficient in time

    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # head: LRU and tail: MRU
        self.head, self.tail = Node(key=-1, val=-1), Node(key=-1, val=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_end(self, node) -> None:
        print("MOVE node", node)
        if node is self.tail.prev:
            return  # Already at the end
        self._remove(node)
        self._insert(node)
        return node.val

    def _insert(self, node: Node):
        """
        example 
        H <-> 1 <-> T
        insert 2
        step 1: 1 <--2--> T (next and prev of new node)
        step 2: 1-->2 && 2<--T (next and prev of existing nodes)
        """
        prev = self.tail.prev
        print(f"prev={prev}, next={self.tail}, node={node}")
        print(f"node_prev={prev}, node_next={self.tail}")
        node.prev, node.next = prev, self.tail
        print(f"node_prev={prev}, node_next={self.tail}")
        # prev.next = self.tail.prev = node
        self.tail.prev = prev.next = node

    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int):
        if not (key in self.cache):
            return -1
        node: Node = self.cache[key]
        self._move_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        print(f"PUT key={key}, value={value}")
        if key in self.cache:
            # update existing value
            print(f"self.cache={self.cache}, key={key}")
            node = self.cache[key]
            node.val = value
            self._move_to_end(node)
        else:
            node: Node = Node(key=key, val=value)
            self.cache[key] = node
            self._insert(node)
            print(self.cache)
            # self.head.display()
            if len(self.cache) > self.capacity:
                print("REMOVING ...")
                next_remove: Node = self.head.next
                self._remove(next_remove)
                self.cache.pop(next_remove.key)

    def display(self):
        cur = self.head
        print("--------------DISPLAY-----------------------------")
        while cur:
            print(f"cur=[{cur.key}:{cur.val}]")
            cur = cur.next
        print("--------------END-----------------------------")


class LRUCacheOrderedDict:
    """
    time complexity for put and get O(1)

    time complexity O(N)

    notes:
        - OrderedDict() acts as a doubly linkedlist with dictionnary properties
             where it keeps order of items insertion
        - this solutions beats 97% in runtime and 76% in memory


    """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end[key]
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # must be first before `self.cache[key] = value`
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # to pop in FIFO order


def get_class(capacity) -> Union[LRUCacheLLV2, LRUCacheOrderedDict]:
    return LRUCacheLLV2(capacity)

# lru_cache = get_class(2)
# lru_cache.put(1, 0)
# lru_cache.put(2, 2)
# print("HERE")
# print("GET")
# lru_param = lru_cache.get(1)
# assert lru_param == 0
# lru_cache.display()

# # print("@@@@ HEAD @@@@")
# # lru_cache.head.display()

# lru_cache.put(3, 3)
# print("@@@@ HEAD @@@@")
# lru_cache.display()


# lru_param = lru_cache.get(2)
# assert lru_param == -1
# lru_cache.put(4, 4)
# print("@@@@ HEAD @@@@")
# lru_cache.display()


# lru_param = lru_cache.get(1)
# assert lru_param == -1
# lru_cache.display()
# lru_param = lru_cache.get(3)
# assert lru_param == 3
# lru_cache.display()
# lru_param = lru_cache.get(4)
# assert lru_param == 4
# lru_cache.display()


# lru_cache = get_class(1)
# lru_cache.put(2, 1)
# lru_cache.display()
# lru_param = lru_cache.get(2)
# assert lru_param == 1
# lru_cache.display()

# lru_cache.put(3, 2)
# lru_cache.display()
# lru_param = lru_cache.get(2)
# assert lru_param == -1
# lru_param = lru_cache.get(3)
# assert lru_param == 2


lru_cache = get_class(2)
lru_cache.put(2, 1)
lru_cache.put(2, 2)
lru_cache.display()
lru_param = lru_cache.get(2)
assert lru_param == 2
lru_cache.display()
lru_cache.put(1, 1)
lru_cache.put(4, 2)
lru_cache.display()
lru_param = lru_cache.get(2)
assert lru_param == -1

