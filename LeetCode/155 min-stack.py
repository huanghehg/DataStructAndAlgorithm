# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
#  
#
# 示例:
#
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
#
# 提示：
#
# pop、top 和 getMin 操作总是在 非空栈 上调用。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-stack
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min is None:
            self.min = x
            return
        if self.min > x:
            self.min = x

    def pop(self) -> None:
        if len(self.stack) > 0:
            item = self.stack.pop()
            if item == self.min:
               if len(self.stack) != 0:
                   self.min = self.stack[0]
                   for index in range(1, len(self.stack)):
                       if self.min < self.stack[index]:
                           continue
                       self.min = self.stack[index]
               else:
                   self.min = None


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min




# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = [math.inf]
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.min_stack.append(min(x, self.min_stack[-1]))
#
#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min_stack[-1]
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/min-stack/solution/zui-xiao-zhan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

