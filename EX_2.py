a, b, c, d = map(int, input().split())

out_filter = list(filter(lambda x: x if x % c == 0 and x % d == 0 else 0, range(a, b + 1)))
sum_out_filter = sum(out_filter)
print(sum_out_filter)
