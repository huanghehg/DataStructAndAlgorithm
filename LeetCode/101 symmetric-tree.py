# 给定一个二叉树，检查它是否是镜像对称的。
#
#  
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        return self.check(root.left, root.right)
        pass

    def check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None  or node2 is None:
            return False

        return node1.val == node2.val and self.check(node1.left, node2.right) and self.check(node1.right, node2.left)


    #     if root is None: return True
    #     return self.check([root])
    #
    # def check(self, stack: list):
    #     isAllNull = True
    #     arr = []
    #     i, j = 0, len(stack) - 1
    #     while i < j:
    #         if stack[i] is not None and stack[j] is not None and stack[i].val == stack[j].val:
    #             i += 1
    #             j -= 1
    #             isAllNull = False
    #             continue
    #         if stack[i] is None and stack[j] is None:
    #             i += 1
    #             j -= 1
    #             continue
    #         return False
    #     if i == j and isAllNull is True:
    #         if stack[i] is None:
    #             return True
    #         else:
    #             isAllNull = False
    #     if isAllNull: return True
    #     for item in stack:
    #         if item is None:
    #             arr += [None, None]
    #             continue
    #         arr.append(item.left)
    #         arr.append(item.right)
    #     return self.check(arr)


if __name__ == '__main__':
    node1 = TreeNode("1")
    node2 = TreeNode("2")
    node3 = TreeNode("2")
    node4 = TreeNode("3")
    node5 = TreeNode("3")
    node6 = TreeNode("4")
    node7 = TreeNode("4")

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node6

    node3.left = node5
    node3.right = node7

    print(Solution().isSymmetric(node1))
