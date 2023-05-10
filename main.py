def bin_to_dec(num):
    """Converts a binary number to decimal."""
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * 2**(len(num)-1-i)
    return decimal


def oct_to_dec(num):
    """Converts an octal number to decimal."""
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * 8**(len(num)-1-i)
    return decimal


def hex_to_dec(num):
    """Converts a hexadecimal number to decimal."""
    decimal = 0
    for i in range(len(num)):
        if num[i].isdigit():
            decimal += int(num[i]) * 16**(len(num)-1-i)
        else:
            decimal += (ord(num[i])-55) * 16**(len(num)-1-i)
    return decimal


def dec_to_bin(num):
    """Converts a decimal number to binary."""
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary


def dec_to_oct(num):
    """Converts a decimal number to octal."""
    octal = ""
    while num > 0:
        octal = str(num % 8) + octal
        num //= 8
    return octal


def dec_to_hex(num):
    """Converts a decimal number to hexadecimal."""
    hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexa = ""
    while num > 0:
        remainder = num % 16
        if remainder in hex_dict:
            hexa = hex_dict[remainder] + hexa
        else:
            hexa = str(remainder) + hexa
        num //= 16
    return hexa


def convert(num):
    """Converts a number to decimal and then to the desired system/"""
    if num.isdigit():
        decimal = int(num)
    elif num.isalpha() and all(c in "0123456789ABCDEFabcdef" for c in num):
        decimal = hex_to_dec(num.upper())
    else:
        for c in num:
            if c not in "0123456789ABCDEFabcdef":
                return "Error: invalid input"
        decimal = int(num, 2)
    print("Decimal representation:", decimal)
    print("Binary representation:", dec_to_bin(decimal))
    print("Octal representation:", dec_to_oct(decimal))
    print("Hexadecimal representation:", dec_to_hex(decimal))


if __name__ == "__main__":
    num = input("Enter a number in binary, "
                "octal, decimal, or hexadecimal format: ")
    convert(num)
