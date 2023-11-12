def solve(s):
    name = s.split()
    return " ".join(n.capitalize() for n in name)
    
    # You can use title() method if there is no condition with numeric thing
