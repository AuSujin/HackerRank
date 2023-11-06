def swap_case(s):
    swapped = ""
    for a in s:
        if a.isupper():
            swapped+=a.lower()
        elif a.islower():
            swapped+=a.upper()
        else:
            swapped+=a
    return swapped

# There is a method for executing exact same thing
def swap_case(s):
    return s.swapcase()
