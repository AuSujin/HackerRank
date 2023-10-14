# The * is used to grab additional returns from split statement.
# string.format()

N = int(input())
student_marks = {}

for _ in range(N):
  name, *rest = input().split()
  student_marks[name] = list(map(float, rest))

query_name = input()

query_average = sum(student_marks[query_name]) / 3
print("{qa:.2f}".format(qa=query_average))
