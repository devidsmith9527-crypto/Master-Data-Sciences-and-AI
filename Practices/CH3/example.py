def is_balanced(expr):
    stack = []
    for char in expr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            stack.pop()  # ដកអាបើកចុងក្រោយចេញមកផ្ទឹម
    return len(stack) == 0


print("កូដ (a + b) * [c] ត្រឹមត្រូវទេ?", is_balanced("(a + b) * [c]"))
print("កូដ (a + b] ត្រឹមត្រូវទេ?", is_balanced("(a + b]"))
