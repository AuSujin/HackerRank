def average(array):
    heights = set(array)
    return '{:.3f}'.format(sum(heights) / len(heights))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
