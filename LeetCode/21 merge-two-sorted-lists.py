# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
#  
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        cur = l1
        pre = None
        head = l1
        while l1 is not None and l2 is not None:
            if l2.val < l1.val:
                next = l2.next
                l2.next = l1
                if pre is not None:
                    pre.next = l2
                else:
                    head = l2
                pre = l2
                l2 = next
            else:
                pre = l1
                l1 = l1.next
        if l1 is None and pre is not None: pre.next = l2
        return head





