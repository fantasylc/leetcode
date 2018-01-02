"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pow = 0
        l_1 = 0
        while l1:
            l_1+=l1.val*(10**pow)
            pow += 1
            l1 = l1.next
        l_2 = 0
        pow = 0
        while l2:
            l_2+=l2.val*(10**pow)
            pow += 1
            l2 = l2.next
        res = l_1 + l_2
        if res < 10:
            return ListNode(res)
        list_res = []
        while res:
            res,v = divmod(res, 10)
            list_res.insert(0, v)
        node = ListNode(list_res[0])
        for i in range(1,len(list_res)):
            new_node = ListNode(list_res[i])
            new_node.next = node
            node = new_node
        return node