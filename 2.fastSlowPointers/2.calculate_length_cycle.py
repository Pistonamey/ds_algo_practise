class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def has_cycle(head):
    slowPointer=head
    fastPointer=head

    while(fastPointer and fastPointer.next):
        if slowPointer==fastPointer.next.next:
            return calculateLength(slowPointer)
        
        slowPointer=slowPointer.next
        fastPointer=fastPointer.next.next

    return False

def calculateLength(slowPointer):
    current=slowPointer
    length=0
    while(True):
        length+=1
        current=current.next
        if(current==slowPointer):
            return length
    
def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(6)
    print("LinkedList has cycle: "+str(has_cycle(head)))

    head.next.next.next.next.next.next=head.next.next
    print("LinkedList has cycle: "+str(has_cycle(head)))

    head.next.next.next.next.next.next=head.next.next.next
    print("LinkedList has cycle: "+str(has_cycle(head)))

main()
