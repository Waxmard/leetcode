from typing import List


def solution(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    common_prefix = strs[0]
    if common_prefix == "":
        return ""

    for cur_string in strs[1:]:

        if cur_string == "":
            return ""

        # if ever the first char doesn't match there is no common prefix
        if common_prefix[0] != cur_string[0]:
            return ""

        # cut off any extra characters either strings have
        min_len = min(len(common_prefix), len(cur_string))
        common_prefix = common_prefix[:min_len]
        cur_string = cur_string[:min_len]

        # remove all non matching characters, must all match from left to right
        for i in range(1, min_len):
            if common_prefix[i] != cur_string[i]: # if non match found, common prefix is everything before
                common_prefix = common_prefix[:i]
                break
    return common_prefix

print(solution(["flower","flow","flight"]))
print(solution(["dog","racecar","car"]))
