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

    def display(self):
        nodes = []
        ptr = self.head
        while ptr:
            nodes.append(str(ptr.value))
            ptr = ptr.next
        print(" , ".join(nodes))

    def search(self, item):
        ptr = self.head
        while ptr:
            if ptr.value != item:
                if ptr.next == None:
                    return False
                ptr = ptr.next
            else: 
                return True

    def searchByIndex(self, pos):
        count = 0
        ptr = self.head
        while count != pos:
            if ptr.next == None:
                return None
            ptr = ptr.next
            count += 1
        return ptr

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def size(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def append(self, item):
        new_node = ListNode(item)
        if not self.head:
            self.head = new_node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node

    def index(self, item):
        count = 0
        ptr = self.head
        while ptr:
            if ptr.value != item:
                if ptr.next == None:
                    return None
                ptr = ptr.next
                count += 1
            else: 
                return count
                
    def insert(self, pos, item):
        if pos < 0:
            return
        if pos == 0:
            self.add(item)
            return
        if pos == (self.size()):
            self.append(item)
            return
        if pos > (self.size()):
            return
        firstptr = self.searchByIndex(pos - 1)
        secondptr = self.searchByIndex(pos)
        new_node = ListNode(item)
        firstptr.next = new_node
        new_node.next = secondptr

    def pop(self):
        ptr = self.searchByIndex(self.size() - 1).value
        ptrBefore = self.searchByIndex(self.size() - 2)
        ptrBefore.next = None
        return ptr

    def poppos(self, pos):
        count = 0
        ptr = self.head
        lastptr = None
        while ptr:
            if count != pos:
                if ptr.next == None:
                    return
                lastptr = ptr
                ptr = ptr.next
                count += 1
            else:
                if lastptr == None:
                    if ptr.next == None:
                        prttemp = ptr
                        ptr = None
                        self.head = None
                        return prttemp.value
                    else: 
                        self.head = ptr.next
                        prttemp = ptr
                        ptr = None
                        return prttemp.value
                else:
                    if ptr.next == None:
                        prttemp = ptr
                        ptr = None
                        lastptr.next = None
                        return prttemp.value
                    else:
                        lastptr.next = ptr.next
                        prttemp = ptr
                        ptr = None
                        return prttemp.value
                    
    def __str__(self):
        elements = []
        ptr = self.head
        while ptr:
            elements.append(repr(ptr.value))
            ptr = ptr.next
        return "[" + ", ".join(elements) + "]"
    
    def slice(self, start, stop):
        new_list = List()
        count = 0
        ptr = self.head
        while ptr:
            if start <= count < stop:
                new_list.append(ptr.value)
            elif count >= stop:
                break
            ptr = ptr.next
            count += 1
        return new_list



smth = List()

print(smth.isEmpty())
print(smth.size())
smth.add(4)
smth.add(2)
smth.add(1)
smth.display()
smth.append(5)
print(smth.index(5))
smth.display()
print(smth.search(5))
print(smth.size())
smth.display()
smth.remove(1)
smth.display()
print(smth.isEmpty())
smth.remove(4)
smth.display()
smth.remove(2)
smth.display()
print(smth.index(5))
smth.remove(5)
smth.display()
print(smth.isEmpty())
print(smth.size())
smth.insert(0, 5)
smth.insert(1, 4)
smth.insert(0, 5)
smth.display()
print(smth.pop())
smth.display()
print(smth.poppos(1))

print(smth)
smth.add(4)
smth.add(2)
smth.add(1)
print(smth)
newlist = smth.slice(0, 2)
print(newlist)