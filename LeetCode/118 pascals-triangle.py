# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0: return []
        if numRows == 1: return  [[1]]
        if numRows == 2: return [[1], [1,1]]
        listPre = self.generate(numRows - 1)
        listPreLast = listPre[-1]
        nes = [listPreLast[i] + listPreLast[i + 1] for i in range(len(listPreLast) - 1)]
        nes.insert(0, 1)
        nes.append(1)
        listPre.append(nes)
        return listPre

if __name__ == '__main__':
    print(Solution().generate(0))
    print(Solution().generate(1))
    print(Solution().generate(2))
    print(Solution().generate(3))
    print(Solution().generate(4))
    print(Solution().generate(5))
    print(Solution().generate(6))
