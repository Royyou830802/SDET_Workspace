import pytest

from .solution import Solution, ListNode

@pytest.fixture(scope = "module")
def solution():
    return Solution()

class TestRemoveNthNodeFromEndOfList_HappyPath:
    def test_happy_path(self, solution: Solution):
        head = ListNode(val = 5)
        head = ListNode(val = 4, next = head)
        head = ListNode(val = 3, next = head)
        head = ListNode(val = 2, next = head)
        head = ListNode(val = 1, next = head)
        head = solution.removeNthFromEnd(head, 2)
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        assert result == [1,2,3,5]

