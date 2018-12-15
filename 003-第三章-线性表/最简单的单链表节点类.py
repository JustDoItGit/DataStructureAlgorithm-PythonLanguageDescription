class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


llist1 = LNode(1)
p = llist1

for i in range(2, 11):
    p.next_ = LNode(i)
    p = p.next_

p = llist1

# while p is not None:
while p:
    print(p.elem)
    p = p.next_

print(llist1)
