def is_balanced(S: str) -> bool:
    stack = []
    match = {')': '(', '}': '{', ']': '['}
    for char in S:
        if char in match.values():
            stack.append(char)
        elif char in match:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("[()]()("))

