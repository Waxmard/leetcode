from leetcode_imports import *


def attempt(s: str) -> int:
    max_len = 0
    char_index_map = {}  # {char, index}
    a = 0

    for i, char in enumerate(s):
        # repeat char, slide window 1 to the right
        if char in char_index_map and char_index_map[char] >= a:
            a = char_index_map[char] + 1

        char_index_map[char] = i

        # update with previous max vs current window length
        max_len = max(max_len, i - a + 1)
    return max_len


run(attempt("dvdf"), 3)
run(attempt("abcabcbb"), 3)
run(attempt("bbbbb"), 1)
run(attempt("pwwkew"), 3)
