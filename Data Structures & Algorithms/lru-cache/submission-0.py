class ListNode:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: "ListNode | None" = None
        self.next: "ListNode | None" = None


class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next



class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.dll = DoubleLinkedList()     
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        node = self.data[key]
        self.dll.remove(node)
        self.dll.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.value = value
            self.dll.remove(node)
        else:
            node = ListNode(key, value)

        self.dll.insert(node)
        self.data[key] = node

        if len(self.data) > self.capacity:
            least_used = self.dll.tail.prev
            del self.data[least_used.key]
            self.dll.remove(least_used)

