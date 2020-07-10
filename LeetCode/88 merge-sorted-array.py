# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#  
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#  
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if m == 0 or n == 0: nums1 += nums2
        # nums1_copy = nums1[:m]
        # nums1[:] = []
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1_copy[i] < nums2[j]:
        #         nums1.append(nums1_copy[i])
        #         i += 1
        #     else:
        #         nums1.append(nums2[j])
        #         j += 1
        # if i < m:
        #     nums1 += nums1_copy[i:]
        # if j < n:
        #     nums1 += nums2[j:]
        # print(nums1)

        p1 = m - 1
        p2 = n - 1
        last = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]


if __name__ == '__main__':
    print(Solution().merge([2, 2, 3, 0, 0, 0, 0], 3, [1, 2, 5, 6], 4))
