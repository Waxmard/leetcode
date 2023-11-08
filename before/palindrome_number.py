
def isPalindrome(x: int) -> bool:
    num = x
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    new = 0
    while x > 0:
        lastDigit = x % 10
        new = new * 10 + lastDigit
        x = x // 10 # remove last digit
    return num == new

print(isPalindrome(10501))
