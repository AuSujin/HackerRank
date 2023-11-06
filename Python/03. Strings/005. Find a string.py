def count_substring(string, sub_string):
    count = 0
    idx = -1
    
    while (string.find(sub_string, idx+1, len(string)) != -1):
        count += 1
        idx = string.find(sub_string, idx+1, len(string))
        
    return count
