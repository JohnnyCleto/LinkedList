from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("list index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, elem):
        if index < 0 or index >= self._size:
            raise IndexError("list index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = elem

    def index(self, elem):
        current = self.head
        idx = 0
        while current:
            if current.data == elem:
                return idx
            current = current.next
            idx += 1
        raise ValueError(f"{elem} is not in list")

    def insert_at_position(self, index, elem):
        if index < 0 or index > self._size:
            raise IndexError("list index out of range")
        
        new_node = Node(elem)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1

    def remove(self, elem):
        if not self.head:
            raise ValueError(f"{elem} not found in the list")
        
        if self.head.data == elem:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.data != elem:
                current = current.next

            if current.next is None:
                raise ValueError(f"{elem} not found in the list")
            
            current.next = current.next.next

        self._size -= 1

    def __str__(self):
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))  
            current = current.next
        
        return "->".join(elements)


