# Write a function to round an int value up to the next multiple of 10 if its rightmost digit is 5 or more. 
# So 15 rounds up to 20, and 6 rounds up to 10. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values.

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(a, b, c):
    
    return round_num(a) + round_num(b) + round_num(c)


def round_num(value):
    remainder = value % 10 
    if remainder < 5:
        return value - remainder
    else:
        return value + (10 - remainder)

## Incorrect b/c the problem is asking to round the values BEFORE you sum them
# def round_sum(a, b, c):
#     # first sum the values
#     sumNum = a + b + c

#     # get the ending digit of the sum value
#     # if the end digit is  < 5 make the digit 0
#     remainder = sumNum % 10
#     if remainder < 5:
#         sumNum -= remainder
#     else: # if end digit >= 5 round up
#         sumNum += (10-remainder)

#     return sumNum