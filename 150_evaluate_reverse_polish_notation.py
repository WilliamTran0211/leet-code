tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = [
    "-78",
    "-33",
    "196",
    "+",
    "-19",
    "-",
    "115",
    "+",
    "-",
    "-99",
    "/",
    "-18",
    "8",
    "*",
    "-86",
    "-",
    "-",
    "16",
    "/",
    "26",
    "-14",
    "-",
    "-",
    "47",
    "-",
    "101",
    "-",
    "163",
    "*",
    "143",
    "-",
    "0",
    "-",
    "171",
    "+",
    "120",
    "*",
    "-60",
    "+",
    "156",
    "/",
    "173",
    "/",
    "-24",
    "11",
    "+",
    "21",
    "/",
    "*",
    "44",
    "*",
    "180",
    "70",
    "-40",
    "-",
    "*",
    "86",
    "132",
    "-84",
    "+",
    "*",
    "-",
    "38",
    "/",
    "/",
    "21",
    "28",
    "/",
    "+",
    "83",
    "/",
    "-31",
    "156",
    "-",
    "+",
    "28",
    "/",
    "95",
    "-",
    "120",
    "+",
    "8",
    "*",
    "90",
    "-",
    "-94",
    "*",
    "-73",
    "/",
    "-62",
    "/",
    "93",
    "*",
    "196",
    "-",
    "-59",
    "+",
    "187",
    "-",
    "143",
    "/",
    "-79",
    "-89",
    "+",
    "-",
]  # 165


"""
Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 
"""


operators = ["+", "-", "*", "/"]

operation_stack = []
for tok in tokens:
    if tok.split("-")[-1].isdecimal():
        operation_stack.append(float(tok))
        print(tok, "=>", operation_stack)
    else:
        second = operation_stack.pop()
        first = operation_stack.pop()
        print("cal: ", operation_stack, "=>", second, tok, first)
        if tok == "+":
            result = second + first
        elif tok == "-":
            result = first - second
        elif tok == "*":
            result = first * second
        elif tok == "/":
            result = int(first / second)

        operation_stack.append(result)
        print("fin cal: ", operation_stack)

print(int(operation_stack.pop()))
