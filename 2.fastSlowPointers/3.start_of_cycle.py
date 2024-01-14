class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow=head
    fast=head

    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        if(fast==slow):
            length_of_cycle=calculate_cycle_length(slow)
            return get_start_of_cycle(length_of_cycle,head)
    return False

def calculate_cycle_length(slow):
    current=slow

    current=current.next
    cnt=1
    while(current!=slow):
        current=current.next
        cnt+=1
    return cnt

def get_start_of_cycle(cnt,head):
    pt1=head
    pt2=head
    while(cnt>0):
        pt2=pt2.next
        cnt-=1
    while(pt2!=pt1):
        pt2=pt2.next
        pt1=pt1.next
    
    return pt1.value


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: "+str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: "+str(has_cycle(head)))

    head.next.next.next.next.next.next = head
    print("LinkedList has cycle: "+str(has_cycle(head)))


main()
