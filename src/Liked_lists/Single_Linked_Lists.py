class Node:

    def __init__(self):
        self.data = None
        self.next = None

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def len(self):
        if self.head is None:
            return 0
        else:
            i=0
            curr= self.head
            while curr is not None:
                i=i+1
                curr=curr.next
            return i



    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        if current == None:
            current = new_node
        else:
            while current.next != None:
                current = current.next

            current.next = new_node

    def dispay(self):
        curr = self.head

        while curr != None:
            print(curr.data)
            curr = curr.next

    def insert_at_nth(self, data, index):
        new_node = Node(data)
        i = 0
        curr = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            print("Current LL doesnot have any node,hence adding it in the first")
            return
        if index >= self.len():
            print("index out of range at node at the end: ",index,self.len())
            while curr.next != None:
                curr = curr.next
            curr.next=new_node

            return
        while curr.next != None:
            i = i + 1
            if (i == index):
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next


ll = LinkedList()
ll.insert_at_begin(10)
ll.insert_at_end(20)
ll.insert_at_end(70)
ll.insert_at_nth(30,3)
ll.dispay()
