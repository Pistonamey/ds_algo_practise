class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def palindrome_list(head):
    if head is None or head.next is None:
        return True

    slow=head
    fast=head

    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    
    second_half=reverse(slow)
    copy_half=second_half

    while(second_half!=None and head!=None):
        if(head.value!=second_half.value):
            break
        second_half=second_half.next
        head=head.next
    
    reverse(second_half)

    if(head is None or second_half is None):
        return True
    return False
def reverse(head):
    current=head
    next=None
    prev=None

    while(current!=None):
        next=current.next
        current.next=prev
        prev=current
        current=next
    
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    last_node=head.next.next.next.next
    print("Middle Node: "+str(palindrome_list(head)))

    last_node.next=Node(2)
    print("Middle Node: "+str(palindrome_list(head)))
main()