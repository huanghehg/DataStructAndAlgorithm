#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
class Solution:
    def isValid(self, s: str) -> bool:
        if s is None: return False
        if len(s) == 0: return True
        stack = []
        for k in s:
            if k == "(" or k == "{" or k == "[":
                stack.append(k)
                continue
            if len(stack) == 0:
                return False
            if (k == ")" and stack[-1] == "(") or (k == "}" and stack[-1] == "{") or (k == "]" and stack[-1] == "["):
                stack.pop()
            else:
                return False
                pass
        return len(stack) == 0