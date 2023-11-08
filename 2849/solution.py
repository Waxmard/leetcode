from leetcode_imports import *


def isReachableAtTime(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    """ "
    t is non negative (time)
    """
    # edge case
    if sx == fx and sy == fy and t == 1:
        return False

    return t >= max(abs(fx - sx), abs(fy - sy))
    a = abs(fx - sx)
    b = abs(fy - sy)
    c = floor(sqrt(a**2 + b**2))

    # edge case
    if c == 0 and t == 1:
        return False

    print(t, c)
    return t >= c


run(isReachableAtTime(5, 1, 1, 4, 4), True)
run(isReachableAtTime(1, 2, 1, 2, 1), False)
run(isReachableAtTime(1, 1, 2, 2, 1), True)
run(isReachableAtTime(2, 4, 7, 7, 6), True)
run(isReachableAtTime(3, 1, 7, 3, 3), False)
