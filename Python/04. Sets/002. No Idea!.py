if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = input().split()
    A = set(input().split())
    B = set(input().split())
    
    score = 0
    for i in arr:
        if i in A:
            score += 1
        elif i in B:
            score -= 1
            
    print(score)


    # we can shorten above like this
    print(sum((i in A) - (i in B) for i in arr))
