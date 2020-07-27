# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def mySqrt(self, x: int) -> int:
        max = x
        min = 0
        i = x // 2
        while min < max:
            if i * i > x:
                max = i - 1
            elif (i + 1) * (i + 1) < x:
                min = i + 1
            else:
                return i + 1 if (i + 1) * (i + 1) == x else i
            i = (max + min) // 2

        return min

if __name__ == '__main__':
    print(Solution().mySqrt(100000000))
    print(Solution().mySqrt(0))
    print(Solution().mySqrt(1))
    print(Solution().mySqrt(2))