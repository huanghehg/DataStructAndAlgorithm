# coding=utf-8
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        curIndex = 1
        cur = head
        pre = None
        rootHead = head
        while curIndex < m:
            pre = cur
            cur = cur.next
            curIndex += 1
        headM = cur
        while curIndex <= n:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            curIndex += 1
        if headM.next is not None:
            headM.next.next = pre
        else:
            rootHead = pre
        headM.next = cur
        return rootHead



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
    print(Solution().reverseBetween(node1, 2, 7))
