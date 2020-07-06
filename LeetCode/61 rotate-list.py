# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-list
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0: return head
        if head is None: return None
        top = head
        count = 1
        while head.next is not None:
            count += 1
            head = head.next
        if k % count == 0: return top
        index = count - k % count
        last = top
        for i in range(index - 1):
            last = last.next
        head.next = top
        top = last.next
        last.next = None
        return top
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
    print(Solution().rotateRight(node1, 3))