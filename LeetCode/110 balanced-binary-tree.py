# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balanced-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self._deepMap = {}
        pass

    @property
    def deepMap(self):
        return self._deepMap

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None: return True
        return abs(self.deep(root.left) - self.deep(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(
            root.right)

    def deep(self, node):
        if node is None:
            return 0
        if node in self.deepMap:
            return self.deepMap[node]
        deep = 1 + max(self.deep(node.left), self.deep(node.right))
        self.deepMap[node] = deep
        return deep
