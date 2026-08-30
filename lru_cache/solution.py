class LRUCache:
    # declareing doubly LL
    class ListNode:
        def __init__(self, key = None, val=None,  next = None, prev = None):
            self.val = val
            self.key = key
            self.next = next
            self.prev =prev

    def __init__(self, capacity: int):
        self.limit = capacity
        self.hmap = {}

        # dummy head and tail
        self.head = self.ListNode()
        self.tail = self.ListNode()

        # connecting
        self.head.next = self.tail
        self.tail.prev = self.head


# ----------------------------------
    # user-defined functionsss
    def addFront(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    
    # to remove
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # moving to front using above two func
    def moveToFront(self, node):
        self.delete(node)
        self.addFront(node)
    
    def deleteBack(self):
        # setting tail to 2nd last
        lru = self.tail.prev

        # just removing last
        self.delete(lru)

        return lru

# -----------------------------------------------------------------
    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1

        self.moveToFront(self.hmap[key])
        return self.hmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.moveToFront(node)
        else:
            if len(self.hmap) == self.limit:
                lru = self.deleteBack()
                del self.hmap[lru.key]
                
            
            newNode = self.ListNode(key, value)
            self.hmap[key] = newNode
            self.addFront(newNode)
      


        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)