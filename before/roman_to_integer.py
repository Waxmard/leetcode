
def solution(s: str):
    translations = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    special = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    special_starters = {'I', 'X', 'C'}
    total = 0
    buffer = ''

    for char in s:
        buffer += char # build buffer
        print(char, buffer, total)

        if len(buffer) == 1:
            if buffer not in special_starters: # special case could be possible
                total += translations[buffer] # not special, update total and reset buffer
                buffer = ''
        else:
            if buffer in special: # check for special case first, if found, add total and reset buffer
                total += special[buffer]
                buffer = ''
            else: # update the total with the first character
                total += translations[buffer[0]]
                buffer = buffer[1]

    print(buffer, total)
    if len(buffer) > 0: # if remaining, use the characters
        if buffer in special:
            total += special[buffer]
            buffer = ''
        else:
            for b in buffer:
                total += translations[b]
                buffer = ''

    return total

print('solution is ', solution('III'))
print('solution is ', solution('MCMXCIV'))
print('solution is ', solution('MCMXCVI'))
print('solution is ', solution('MDCCCLXXXIV'))
