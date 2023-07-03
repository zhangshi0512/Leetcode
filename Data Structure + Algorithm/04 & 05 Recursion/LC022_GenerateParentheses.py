"""
22. Generate Parentheses

Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
"""

def generateParenthesis(n):
    res = []
    def backtrack(left, right, S):
        # left代表当前S中的左括号数量
        # right代表当前S中的右括号数量

        # base case: len(S) == n * 2 返回结果
        if len(S) == n*2:
            res.append(S)
            return
        else:
            # 试探添加左括号
            if left < n:
                backtrack(left + 1, right, S + "(")
            # 试探添加右括号
            if left > right:
                backtrack(left, right + 1, S + ")")

    backtrack(0, 0, "")
    return res

print("Expected:", ["((()))","(()())","(())()","()(())","()()()"])
print("Actual:", generateParenthesis(3))
print("Expected:", ["()"])
print("Actual:", generateParenthesis(1))
