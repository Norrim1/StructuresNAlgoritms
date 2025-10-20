from weakref import ref


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
                    
    def reverse_iterative(self):
        lastptr = None
        ptr = self.head

        while ptr:
            next_ptr = ptr.next
            ptr.next = lastptr 
            lastptr = ptr        
            ptr = next_ptr 

        return lastptr
    
    def __str__(self):
        elements = []
        ptr = self.head
        while ptr:
            elements.append(repr(ptr.value))
            ptr = ptr.next
        return "[" + ", ".join(elements) + "]"


smth = List()
smth.add(5)
smth.add(4)
smth.add(3)
smth.add(2)
smth.add(1)
print(smth)