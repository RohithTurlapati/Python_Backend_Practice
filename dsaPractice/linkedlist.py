# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

#     def __str__(self):
#         return str(self.value)
    

# Head = Node(4)
# A = Node(5)
# B = Node(7)
# C = Node(1)

# Head.next = A
# A.next = B
# B.next = C

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

Head = Tail = Node(1)

def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.value))
        curr = curr.next
    
    return "<->".join(element)


def insert_at_begin(head, val):
    new = Node(val, next=head)
    head.prev = new
    
    return new, Tail

Head, Tail = insert_at_begin(Head, 7)

dis = display(Head)
print(dis)
        
