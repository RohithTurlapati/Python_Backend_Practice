# l1 = [1,2,3,4,5,6]

# it = iter(l1)
# print(next(it))

# def reverse_string(word: str) -> str:
#     i = 0
#     j = len(word) -1

#     list_str = list(word)

#     while i < j:
#         list_str[i] , list_str[j] = list_str[j], list_str[i]
#         i += 1
#         j -= 1
    
#     return "".join(list_str)


# print(reverse_string("adfsag"))


# def is_balanced(S: str) -> bool:
#     stack = []
#     match = {')': '(', '}': '{', ']': '['}
#     for char in S:
#         if char in match.values():
#             stack.append(char)
#         elif char in match:
#             if not stack or stack[-1] != match[char]:
#                 return False
#             stack.pop()
#     return len(stack) == 0

# print(is_balanced("[()]()("))

