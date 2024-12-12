class ListNode:

    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = {}

        self.leastRec = ListNode(0,0)
        self.mostRec = ListNode(0,0)

        self.leastRec.next = self.mostRec
        self.mostRec.prev = self.leastRec

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
            self.insert(self.LRUCache[key])
            return self.LRUCache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
        tempNode = ListNode(key,value)
        self.LRUCache[key] = tempNode
        self.insert(tempNode)

        if len(self.LRUCache) > self.capacity:
            lru = self.leastRec.next
            self.remove(lru)
            del self.LRUCache[lru.key]

        #print(self.LRUCache[key].val)

    def remove(self, node):
        before, after = node.prev, node.next
        before.next, after.prev = after, before

    def insert(self, node):
        # mostRecPrev = self.mostRec.prev
        # self.mostRec.prev = node
        # node.next = self.mostRec
        # mostRecPrev.next = node
        # node.prev = mostRecPrev

        prev, next = self.mostRec.prev, self.mostRec
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
