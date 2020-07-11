# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxSubArray(self, nums: list) -> int:
        if nums is None: return None
        if len(nums) == 0: return None
        # 动态规划
        # pre = nums[0]
        # maxSum = nums[0]
        # for i in range(1, len(nums)):
        #     if pre > 0:
        #         nums[i] = nums[i] + pre
        #     pre = nums[i]
        #     maxSum = max(maxSum, pre)
        #
        # return maxSum

        # 贪心法
        # curSum = nums[0]
        # maxSum = nums[0]
        # for i in range(1, len(nums)):
        #     if (curSum) < 0:
        #         curSum = nums[i]
        #     else:
        #         curSum += nums[i]
        #     maxSum = max(curSum, maxSum)
        # return maxSum


if __name__ == '__main__':
    print(Solution().maxSubArray(None))
