"""
1249. Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lst_s = list(s)
        key = ["(", ")"]

        tmp = []
        for idx, ele in enumerate(lst_s):
            if ele in key:
                if len(tmp) == 0:
                    if ele == ")":
                        lst_s[idx] = ""
                    else:
                        tmp.append((idx, ele))
                else:
                    check_prev = tmp[-1][1]
                    if check_prev != ele:
                        tmp.pop()
                    else:
                        tmp.append((idx, ele))

        if len(tmp) != 0:
            for item in tmp:
                idx, ele = item
                if ele in key:
                    lst_s[idx] = ""

        return "".join(lst_s)


sol = Solution()

s = "lee(t(c)o)de)"
print("ans:  ", sol.minRemoveToMakeValid(s))


s = "a)b(c)d"
print("ans:  ", sol.minRemoveToMakeValid(s))


s = "))(("
print("ans:  ", sol.minRemoveToMakeValid(s))


# s = "(())((((((((()()()((()())((()))))))))((("
# print("ans:  ", sol.minRemoveToMakeValid(s))


s = "a("
print("ans:  ", sol.minRemoveToMakeValid(s))


s = "((("
print("ans:  ", sol.minRemoveToMakeValid(s))

# s = "))()())(())((()((q((()((()((((u))())(o()))))()(((((())))(((())())()x))(())))))()((())())))()(q()(())())))(dp))((nx())g(((()))(()()())x)ih)k()()))(((()()(()(((())q)())))))(((((()()(()()()())k))gx)n))))())()))))))))()))(((((a)q)))))))(t))))(c)()))(()p(()))))(t(()()))))))(cr()))(()()))()((()())())))())()(())))))))())()((((r)()(()r())))g)()())))))((())v)u)()())()))z(())()())(c))vk)((((()(())))))(g(r)()v)(((()))))))))()(h)((((h())))()(((())((()))(()))))()()(()()(()m()))))))x)((()(())))(()g)(())(()()(()r))()()()h)))())))))))))s)(()(()(((()()()b())))())())lx))))k)))p)(()(x))))())(()ca))))))((())())))((()()()))()()v())))()))()()u)))())()))()(()(()))((()((())(()()(()b))(((((()()))((((())))(a))b))(())(())b(b(()()())(()()))(())))(r()))())())))()())a)())))())()())cy(((())u)))(())(k))())((()((()())()(((n)))))(((())))()(()(b)(()))()))()s)))(())))((((()())))()()))(())(()()())))()()())()((vc())p)())))r(()))d)(())()))))()y()(i)())()))n)))((f())())))(()(()z((()y)((q())(()(()()))))())((nz)()(()()(()((()))))()()())(()(())))))(r))r)()(t)(()()()))(z(()())))))()(r(())())())(()))(w)))rlf)()a)(((()))()))((((()))())()()(()))((()))()))()x))))(((())()()))()))))()((()))rx((z))))())))g)))))o)))()(u)())())))(up))())((())()))(()(c)(()))())((()cz)))()()z))))(()())))))()()x())j))((())()))(()())))))())()))())(x))v())((((((()))))((((t())h())))))j))((()()))))kx)())(()))()))(k))))()d))))))l))()))()(t(q))())))(()))(d)))())(((())(()(()))(()xt))((()(()))))(())((()()))(o(())()()()w()(()((((e))(ff)p()))(())())()()()()(())))(((((()))(()a(())))()))(()())())(()(n)())(()))()))()))(()(h))w)))())))))))()y))y))()()()))((s(((())p))))()((s)(()(()v)()()))(((())()e)(())(())())())(()))))()(j()jl)))))))r())((((()())()())()))))(())()(())))()(()()mm)))r(()))()())()))))())(())())(b()((())u)))))))((()d)(()()))())())()())(((()((())))w))(v)))m(g))))i((()(((())))(())()()((b)())k)()())))(()()))()))))e))))))((()()))())sv()())))((o())())())()))y())))(s))())q)(()(((()))efh)))))((m((()((()())))()))(((l)())q())))()))s)()())(()))())("
# print("ans:  ", sol.minRemoveToMakeValid(s))
