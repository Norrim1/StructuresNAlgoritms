class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"

class List:
    def __init__(self, head=None):
        self.head = head

    def add(self, item):
        new_node = ListNode(item)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            return

    def remove(self, item):
        ptr = self.head
        lastptr = None
        while ptr:
            if ptr.value != item:
                if ptr.next == None:
                    return
                lastptr = ptr
                ptr = ptr.next
            else:
                if lastptr == None:
                    if ptr.next == None:
                        ptr = None
                        self.head = None
                        return
                    else: 
                        self.head = ptr.next
                        ptr = None
                        return
                else:
                    if ptr.next == None:
                        ptr = None
                        lastptr.next = None
                        return
                    else:
                        lastptr.next = ptr.next
                        return
                    
    def move_to_front(self):
        n = int(input("Кол-во строк(т.к. в задаче не было условия завершения)"))

        for i in range(n):
            s = input()
            self.remove(s)
            self.add(s)
        return
    
    def __str__(self):
        elements = []
        ptr = self.head
        while ptr:
            elements.append(repr(ptr.value))
            ptr = ptr.next
        return "[" + ", ".join(elements) + "]"

smth = List()
smth.move_to_front()
print(smth)