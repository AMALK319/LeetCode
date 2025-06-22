        
class ListNode:
    def __init__(self, key, val):
        self.val = [key,val]
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash_map = [ListNode(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        m = len(self.hash_map)
        head = self.hash_map[key%m]
        while head.next:
            if head.next.val[0] == key:
                head.next.val[1] = value
                return
            head = head.next
        head.next = ListNode(key,value)

    def remove(self, key: int) -> None:
        m = len(self.hash_map)
        head = self.hash_map[key%m]
        while head and head.next:
            if head.next.val[0] == key:
                head.next = head.next.next
            head = head.next

    def get(self, key: int) -> int:
        m = len(self.hash_map)
        head = self.hash_map[key%m]
        while head.next:
            if head.next.val[0] == key:
                return head.next.val[1]
            head = head.next
        return -1
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)