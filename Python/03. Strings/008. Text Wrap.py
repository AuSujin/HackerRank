import textwrap
# textwrap.fill() returns a single string
# textwrap.wrap() returns a list

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
    
    # If you want to use wrap method
    # Use (*) to print the list seperated by spaces
    wrapped = textwrap.wrap(string, max_width)
    print(*wrapped, sep="\n")
