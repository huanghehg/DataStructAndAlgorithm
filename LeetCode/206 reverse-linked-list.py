# coding=utf-8
# Definition for singly-linked list.
# 206 反转链表
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        head = self
        des = ''
        while head is not None:
            des = des + head.val + ' -> '
            head = head.next
        des += "NULL"
        return des


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        pre, cur = None, head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

        # # 递归
        # if head is None or head.next is None:
        #     return head
        # rHead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return rHead

        # 栈
        # stack = []
        # while head is not None:
        #     stack.append(head)
        #     head = head.next
        # stack[0].next = None
        # i = 1
        # while i < len(stack) :
        #     stack[i].next = stack[i - 1]
        #     i += 1
        # return stack[-1]


if __name__ == '__main__':
    node1 = ListNode("1")
    node2 = ListNode("2")
    node3 = ListNode("3")
    node4 = ListNode("4")
    node5 = ListNode("5")
    node6 = ListNode("6")
    node7 = ListNode("7")
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print(node1)
    print(Solution().reverseList(node1))
