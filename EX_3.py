a, b, c, d = map(int, input().split())

out_filter = list(filter(lambda x: x if int(x) == x and x > 0 and x % c != 0 and x % 10 == d else 0, range(a, b + 1)))
print(out_filter)
