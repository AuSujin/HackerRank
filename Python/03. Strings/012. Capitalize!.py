def solve(s):
    names = s.split(' ')
    return ' '.join(n.capitalize() for n in names)
    
    # You can use title() method if there is no condition with numeric thing
