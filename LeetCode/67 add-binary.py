# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。
#
#  
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#  
#
# 提示：
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-binary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count = min(len(a), len(b))
        tem = 0
        res = []
        reversedA = "".join(reversed(a))
        reversedB = "".join(reversed(b))
        for i in range(count):
            sum = int(reversedA[i]) + int(reversedB[i]) + tem
            tem = sum // 2
            res.append(sum % 2)
            # if sum == 0:
            #     res.append("0")
            #     tem = 0
            # elif sum == 1:
            #     res.append("1")
            #     tem = 0
            # elif sum == 2:
            #     res.append("0")
            #     tem = 1
            # elif sum == 3:
            #     res.append("1")
            #     tem = 1
        if len(a) == count and len(b) == count:
            if tem == 1:
                res.append(str(tem))
            return "".join(reversed(res))
        longStr = reversedA if len(a) > len(b) else reversedB
        index = count
        while tem == 1 and index < len(longStr):
            if int(longStr[index]) == 0:
                res.append("1")
                tem = 0
            else:
                res.append("0")
                tem = 1
            index += 1
        if index < len(longStr):
            return ("".join(res) + longStr[index:len(longStr)])[::-1]

        res.append(str(tem))
        return "".join(reversed(res))


if __name__ == '__main__':
    print(Solution().addBinary("1011", "1111110"))
