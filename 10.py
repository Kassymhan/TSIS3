def func(s):
    s = s.split()
    LIST = []
    for x in s:
        if x not in LIST:
            LIST.append(x)
    return LIST


def func1(s):
    s = s.split()
    s = list(set(s))
    return s


s = input()
print(func(s))
print(func1(s))
