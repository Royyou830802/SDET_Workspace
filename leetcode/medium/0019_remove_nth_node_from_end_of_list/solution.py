from __future__ import annotations

from typing import Any

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count the length of the node list
        NodeLen = 1
        LenTracker = head
        while LenTracker.next != None:
            LenTracker = LenTracker.next
            NodeLen += 1
        # Prevent the situation when input n >= node length
        if NodeLen == n:
            return head.next
        elif NodeLen < n:
            raise ValueError("Input n is larger than node length!")
        
        # Deal with the normal situation: input n < node length
        slowerPt = head
        fasterPt = head
        for idx in range(n):
            fasterPt = fasterPt.next
        while fasterPt.next != None:
            slowerPt = slowerPt.next
            fasterPt = fasterPt.next
        slowerPt.next = slowerPt.next.next
        return head