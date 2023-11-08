from leetcode_imports import *


def attempt(s: str) -> int:
    max_len = 0

    current_chars = set()
    cur_str_len = 0
    for char in s:
        # update max and reset substring
        if char in current_chars:
            max_len = max(max_len, cur_str_len)
            cur_str_len = 0
            current_chars = set()

        current_chars.add(char)
        cur_str_len += 1
    # last substring has not reset so attempt to update max
    max_len = max(max_len, cur_str_len)

    return max_len


run(attempt("dvdf"), 3)
run(attempt("abcabcbb"), 3)
run(attempt("bbbbb"), 1)
run(attempt("pwwkew"), 3)
