# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-palindrome
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None: return False
        if len(s) < 2: return True
        s = s.replace(" ","").lower()
        head = 0
        last = len(s) -1
        while head < last:
            if not s[head].isdigit() and not s[head].isalpha():
                head += 1
                continue
            if not s[last].isdigit() and not s[last].isalpha():
                last -= 1
                continue
            if s[head] == s[last]:
                head +=1
                last -=1
                continue
            return False
        return True
if __name__ == '__main__':
    print(Solution().isPalindrome("race Aa car"))


