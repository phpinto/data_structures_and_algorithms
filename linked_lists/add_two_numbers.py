# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        curr_node = res
        carry = 0
        
        while l1 is not None or l2 is not None:
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            curr = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            
            curr_node.next = ListNode(curr)
            curr_node = curr_node.next
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry != 0:
            curr_node.next = ListNode(carry)
            
        return res.next