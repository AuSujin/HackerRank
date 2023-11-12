# Method 1: Use bin(), oct(), hex()
def dec_to_bin(x):
    return bin(x)[2:]
    
def dec_to_oct(x):
    return oct(x)[2:]
    
def dec_to_hex(x):
    return hex(x)[2:]

def print_formatted(number):
    width = len(dec_to_bin(number))
    for i in range(1, number+1):
        print(str(i).rjust(width), dec_to_oct(i).rjust(width), dec_to_hex(i).rjust(width), dec_to_bin(i).rjust(width), end=" ")
        print()

# Method 2: Use String.format()
def print_formatted(number):
    width = len('{:b}'.format(number))
    for i in range(1, number+1):
        print('{number:{width}d} {number:{width}o} {number:{width}X} {number:{width}b}'.format(number=i, width=width))
        # If you want to print the hex in lower case, use '{number:{width}x}' instead of X
