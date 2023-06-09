class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    current=head
    maxLength=0
    while(current):
        current=current.next
        maxLength+=1
    
    middle=(maxLength//2)
    secondPointer=head
    while(middle>0):
        middle-=1
        secondPointer=secondPointer.next


    return secondPointer




def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Middle Node: "+str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: "+str(find_middle_of_linked_list(head).value))


    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: "+str(find_middle_of_linked_list(head).value))


main()
