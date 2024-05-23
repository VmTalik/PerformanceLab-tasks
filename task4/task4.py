import sys

file_name = sys.argv[1]

lst = []
with open(file_name) as f:
    for i in f:
        lst.append(int(i))

lst.sort()
m = lst[(len(lst) - 1) // 2]  # медиана
result = 0
for elem in lst:
    result += abs(elem - m)
print(result)
