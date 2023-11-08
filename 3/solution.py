from leetcode_imports import *


def attempt(s: str) -> int:
    max_len = 0

    current_chars = set()
    substr = ""
    for char in s:
        if char in current_chars:
            max_len = max(max_len, len(substr))

            # slice off repeated substring
            repeat_index = substr.find(char)
            for i in range(repeat_index + 1):
                current_chars.remove(substr[i])
            substr = substr[repeat_index + 1 : len(substr)]

        current_chars.add(char)
        substr += char

    # last substring has not reset so attempt to update max
    max_len = max(max_len, len(substr))

    return max_len


run(attempt("dvdf"), 3)
run(attempt("abcabcbb"), 3)
run(attempt("bbbbb"), 1)
run(attempt("pwwkew"), 3)
