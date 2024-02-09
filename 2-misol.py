class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    slow = reverseList(slow)

    while slow:
        if head.val != slow.val:
            return False
        head = head.next
        slow = slow.next
    return True

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
print(isPalindrome(head1))

head2 = ListNode(1)
head2.next = ListNode(2)
print(isPalindrome(head2))