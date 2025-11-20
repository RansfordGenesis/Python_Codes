class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head
        while(end != None and end.next != None):
            middle = middle.next
            end = end.next.next
        return middle
