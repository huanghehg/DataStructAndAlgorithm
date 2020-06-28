# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
# 示例：
#
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#  
#
# 提示：
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-array-by-parity
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def sortArrayByParity(self, A):
        # arr = []
        # for i in A:
        #     if i % 2 == 0:
        #         arr.insert(0, i)
        #     else:
        #         arr.append(i)
        # return arr
        if len(A) <= 1: return A
        head = 0
        last = len(A) - 1
        while head < last:
            if A[head] % 2 == 1 and A[last] % 2 == 0:
                A[head], A[last] = A[last], A[head]
                head += 1
                last -= 1

            if A[head] % 2 == 0:
                head += 1

            if A[last] % 2 == 1:
                last -= 1
        return A
