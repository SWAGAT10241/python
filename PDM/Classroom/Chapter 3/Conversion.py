'''
def float_to_binary(num,precision):
    integer_part = bin(int(num))[2:]
    fraction_part = num-int(num)
    binary_fraction = []
    while fraction_part != 0 and len(binary_fraction) < precision:
        fraction_part *= 2
        bit = int(fraction_part)
        binary_fraction.append(bit)
        fraction_part -= bit
    return f"{integer_part}.{''.join(map(str, binary_fraction))}"
# Example: Convert 10.625 to binary with 3 bits of precision for the fractional part
print(float_to_binary(10.625, 3))  # Expected output: "1010.101"
'''

'''
def float_to_binary(num,precision):
    integer_part = bin(int(num))[2:]
    fraction_part = num-int(num)
    binary_fraction = []
    while fraction_part != 0 and len(binary_fraction) < precision:
        fraction_part *= 2
        bit = int(fraction_part)
        binary_fraction.append(str(bit))
        fraction_part -= bit
    return f"{integer_part}.{''.join(map(str, binary_fraction))}"
print(float_to_binary(10.625, 3))
'''

'''
def bin_to_decimal(binary_str):
    integer_part, fraction_part = binary_str.split('.')
    decimal_value = int(integer_part, 2)
    for i, digit in enumerate(fraction_part):
        decimal_value += int(digit) * (2 ** -(i + 1))
    return decimal_value
print(bin_to_decimal('1010.101'))'
'''
# x = int("100011001111",2)
# print(x)

# import pandas as pd
# df = pd.DataFrame (columns=["CustomerID","Country","State","City","Zip Code"] )
# print(df)

a = 5
b = 6
a = a^b
b = a^b
a = a^b
print(a,b)