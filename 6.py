a = []
for i in range(1, 101):
    a.append(i)
a = filter(lambda x: sum([1 for i in range(1, x + 1) if x % i == 0]) == 2, a)

print(*a)