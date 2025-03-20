class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next

        return len(stack) == 0