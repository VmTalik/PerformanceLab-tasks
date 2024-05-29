from collections import deque
import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

dq = deque(range(1, n + 1))
result = [dq[0]]  # результат - путь из начальных элементов интервалов
dq.rotate(-(m - 1))

while dq[0] != result[0]:
    result.append(dq[0])
    dq.rotate(-(m - 1))

print(''.join(map(str, result)))
