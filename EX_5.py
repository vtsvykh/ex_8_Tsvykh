import functools

start, end, num = map(int, input().split())

list_1 = []
for x in range(start, end + 1):
    if (x ** 0.5).is_integer() and x % num == 0:
        list_1.append(x)

res = functools.reduce(lambda x, y: x * y, list_1)
print(res)
