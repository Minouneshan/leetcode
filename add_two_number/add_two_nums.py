# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:    
    
    d1 = l1; i1 = 0; x1 = 0
    d2 = l2; i2 = 0; x2 = 0
    x1 += (d1.val)*(10**(i1))
    x2 += (d2.val)*(10**(i2)) 
    
    while True:  
        if d1.next == None:
            break
        i1 +=1
        d1 = d1.next
        x1 += (d1.val)*(10**(i1))
        

            
    while True:
        if d2.next == None:
            break
        i2 +=1
        d2 = d2.next
        x2 += (d2.val)*(10**(i2))
        

            
    s = x1 + x2     
    
    num = list(map(int, str(s)))  
    num.reverse()

    tail = head = ListNode(num[0])
    for x in num[1:]:
        tail.next = ListNode(x) # Create and add another node
        tail = tail.next 

        
    return(head)
