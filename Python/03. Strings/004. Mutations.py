def mutate_string(string, position, character):
    # Aprroach 1 : Slice the string and join it back
    return string[:position] + character + string[position+1:]

    # Aprroach 2 : convert the string to a list and change the value
    s = list(string)
    s[position] = character
    return "".join(s)
