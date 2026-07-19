class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr_index = 0
        curr_node = self.head
        while curr_node and curr_index <= index:
            if curr_index == index:
                return curr_node.val
            curr_index += 1
            curr_node = curr_node.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        return None
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        curr_node = prev_node = self.head
        curr_index = 0
        new_node = Node(val)

        if index == 0:
            self.addAtHead(val)
            return None

        while curr_node and curr_index <= index:            
            if curr_index == index:
                new_node.next = curr_node
                prev_node.next = new_node
                return None
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        if curr_index == index:
            self.addAtTail(val)

        return None

    def deleteAtIndex(self, index: int) -> None:
        curr_node = prev_node = self.head
        curr_index = 0 

        if index == 0:
            self.head = curr_node.next
            return None
        
        while curr_node and curr_index <= index:
    
            if curr_index == index:
                if curr_node == self.tail:
                    self.tail = prev_node
                next_node = curr_node.next
                prev_node.next = next_node
                return None
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
            

        return None

    def __str__(self):
        curr_node = self.head
        values = []
        while curr_node:
            values.append(str(curr_node.val))
            curr_node = curr_node.next
        return "->".join(values)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(3)
# obj.addAtHead(34)
# obj.addAtTail(100)
# obj.addAtTail(101)
# obj.addAtHead(103)
# print(obj.get(2))
# print(obj)
# obj.deleteAtIndex(3)
# print(obj)
# print(obj.tail.val)
# param_1 = obj.get(index)

# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)