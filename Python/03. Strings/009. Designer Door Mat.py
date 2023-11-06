if __name__=='__main__':
    N, M = map(int, input().split())
    c = ".|."
    
    # UPPER TRIANGLE
    for i in range(N//2):
        print(((2*i+1)*c).center(M, "-"))
        
    # WELCOME PART
    print("WELCOME".center(M, "-"))
        
    # LOWER TRIANGLE
    for i in range(N//2, 0, -1):
        print(((2*i-1)*c).center(M, "-"))
