# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head # 1 step per turn, while reversing the list
        fast = head # 2 steps per turn
        last1 = None
        last2 = None
        n = 0
        while (fast != None):
            last2 = last1
            last1 = slow
            slow = slow.next
            fast = fast.next
            last1.next = last2
            n += 1
            if (fast != None):
                fast = fast.next
                n += 1
        forward = last1
        backward = slow
        if (n % 2 == 1):
            forward = forward.next
        while (forward != None and backward != None):
            if (forward.val != backward.val):
                return False
            forward = forward.next
            backward = backward.next
        return True

