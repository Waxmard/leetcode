from collections import deque


def solution(s: str) -> bool:
    if len(s) % 2 == 1: # the string is all delimiters, so its length must be even
        return False

    delims = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    stack = deque()

    for char in s:
        if char in delims:
            stack.appendleft(char)
        else: # must be a closing delimiter
            if len(stack) == 0: # closing nothing
                return False
            opener = stack.popleft()
            if not delims[opener] == char:
                return False
    if len(stack) > 0: # leftover openers
        return False
    return True

print(solution("()"))
print(solution("()[]{}"))
print(solution("(]"))
