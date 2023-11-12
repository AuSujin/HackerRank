from itertools import permutations

if __name__=='__main__':
    S, length = input().split()
    
    permuted_list = sorted(list(permutations(S, int(length))))
    
    for _ in permuted_list:
        print(''.join(_))
