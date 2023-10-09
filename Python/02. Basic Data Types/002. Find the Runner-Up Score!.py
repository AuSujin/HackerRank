# using sorted() function with Set
n = int(input())
arr = map(int, input().split())

print(sorted(set(arr))[-2])

# using sorted() function with List -> using Set to remove duplicates from list
n = int(input())
arr = map(int, input().split())

print(sorted(list(set(arr)), reverse=True)[1])

# using sort() function with List -> allocate memory for list, because it sorts the object in-place
n = int(input())
arr = map(int, input().split())

sorted_arr = list(set(arr))
sorted_arr.sort(reverse=True)
print(sorted_arr[1])
