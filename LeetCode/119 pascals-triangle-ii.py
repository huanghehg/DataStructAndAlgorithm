# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def getRow(self, rowIndex: int) -> list:
        # if rowIndex == 0: return [rowIndex]
        # if rowIndex == 1: return [1, 1]
        # pre = self.getRow(rowIndex - 1)
        # cur = []
        # for i in range(len(pre) - 1):
        #     cur.append(pre[i] + pre[i + 1])
        # cur.insert(0, 1)
        # cur.append(1)
        # return cur

        cur = [1] * (rowIndex + 1)
        # i 当前行
        for i in range(2, rowIndex + 1):
            # j 当前行需要变得数
            for j in range(1, i):
                # 倒序填充
                index = i - j
                cur[index] = cur[index] + cur[index - 1]
        return cur
