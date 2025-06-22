class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        m = len(self.hash_set)
        head = self.hash_set[key%m]
        while head.next:
            if head.next.val == key:
                return
            head = head.next
        head.next = ListNode(key)

    def remove(self, key: int) -> None:
        m = len(self.hash_set)
        head = self.hash_set[key%m]
        while head and head.next:
            if head.next.val == key:
                head.next = head.next.next
            head = head.next

    def contains(self, key: int) -> bool:
        m = len(self.hash_set)
        head = self.hash_set[key%m]
        while head.next:
            if head.next.val == key:
                return True
            head = head.next
        return False
        
''' 
class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hash_set '''


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)