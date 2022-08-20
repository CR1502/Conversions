# Defining the functions

# Converting Binary to decimal
def bin_to_dec(d):
    value = 0
    for i in range(len(d)):
        j = d.pop()
        if j == '1':
            value = value + pow(2, i)
    return value


# Converting Decimal to Binary
def dec_to_bin(b):
    value = ""
    while (b > 0):
        value = value + str(b % 2)
        b = b // 2
    value = value[::-1]
    return value

# Converting Binary to Decimal
def bin_to_oct(o):
    value = 0
    d = 0
    for i in reversed(o):
        if i == '1':
            d = d + pow(2, value)
        value = value + 1
    o = ""
    while d > 0:
        o = o +str(d % 8)
        d = d // 8
    o = o[::-1]
    return o

# Converting Octal to Binary
def oct_to_bin(b):
    value = 0
    d = 0
    for i in reversed(b):
        d = d + (int(i) * pow(8, value))
        value += 1
    b = ""
    while d > 0:
        b = b + str(d % 2)
        d = d // 2
    b = b[::-1]
    return b
# Converting Decimal to Hexadecimal
def dec_to_hex(d):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex = ''
    while d > 0:
        r = d % 16
        hex = conversion_table[r] + hex
        d = d // 16
    return hex

# Converting hexadecimal to Decimal
def hex_to_dec(h):
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    value = 0
    d = 0
    for i in reversed(h):
        d = d + (conversion_table[i] * pow(16, value))
        value = value + 1
    return d

# Converting Hexadecimal to Binary
def hex_to_bin(h):
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    value = 0
    d = 0
    for i in reversed(h):
        d = d + (conversion_table[i] * pow(16, value))
        value = value + 1
    h = ""
    while d > 0:
        h = h + str(d % 2)
        d = d // 2
    h = h[::-1]
    return h

# Converting Binary to Hexadecimal
def bin_to_hex(b):
    value = 0
    d = 0
    for i in reversed(b):
        if i == '1':
            d = d + pow(2, value)
        value = value + 1
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}
    hex = ''
    while d > 0:
        r = d % 16
        hex = conversion_table[r] + hex
        d = d // 16
    return hex

# Left Shift
def left_shift(a, b):
    return a << b

# Right Shift
def right_shift(a, b):
    return a >> b