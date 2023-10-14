# To initialize a two-dimensional array: [[0]*col for _ in range(row)]
# use set() to remove duplicates

N = int(input())
records = [[0]*2 for _ in range(N)]

for i in range(N):
    records[i][0] = input()
    records[i][1] = float(input())
    
second_lowest_grade = sorted(set(_[1] for _ in records))[1]
second_lowest_grade_student = [_[0] for _ in records if _[1] == second_lowest_grade]

for k in sorted(second_lowest_grade_student):
    print(k)
