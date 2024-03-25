a, b, c, d = map(int, input().split())

out_filter = list(map(lambda x: int(x) == x and x > 0 and x % c != 0 and x % 10 == d, range(a, b + 1)))
print(sum(out_filter))
