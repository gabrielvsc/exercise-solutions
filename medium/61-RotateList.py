# 61. Rotate List

# Solution O(n)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      if not head: return head

      current = head
      size = 1

      while current.next:
        current = current.next
        size += 1
      
      current.next = head
      k = size - (k % size)

      while k > 0:
        current = current.next
        k -= 1

      head = current.next
      current.next = None

      return head