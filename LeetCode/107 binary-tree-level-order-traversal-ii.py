# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if root is None: return []
        deep = 0
        stack = [[root]]
        values = []
        while deep < len(stack):
            current = stack[deep]
            tem = []
            temValue = []
            for i in current:
                temValue.append(i.val)
                if i.left is not None:
                    tem.append(i.left)
                if i.right is not None:
                    tem.append(i.right)

            values.append(temValue)
            if len(tem) > 0:
                stack.append(tem)
                deep += 1
                continue
            break
        return list(reversed(values))


if __name__ == '__main__':
    node1 = TreeNode("1")
    node2 = TreeNode("2")
    node3 = TreeNode("3")
    node4 = TreeNode("4")
    node5 = TreeNode("5")
    node6 = TreeNode("6")
    node7 = TreeNode("7")

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node6

    node3.left = node5
    node3.right = node7
    print(Solution().levelOrderBottom(node1))
