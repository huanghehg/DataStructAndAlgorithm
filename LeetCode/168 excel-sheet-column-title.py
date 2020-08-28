# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# 示例 1:
#
# 输入: 1
# 输出: "A"
# 示例 2:
#
# 输入: 28
# 输出: "AB"
# 示例 3:
#
# 输入: 701
# 输出: "ZY"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/excel-sheet-column-title
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n, y = divmod(n, 26)
            if y == 0:
                n -= 1
                y = 26
            res = chr(y + 64) + res
        return res

if __name__ == '__main__':
    print(Solution().convertToTitle(1))
    print(Solution().convertToTitle(26))
    print(Solution().convertToTitle(52))
    print(Solution().convertToTitle(200))
    print(Solution().convertToTitle(676))
    print(Solution().convertToTitle(677))




