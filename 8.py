def func(s):
    for i in range(0, len(s)):
        if 0 not in s[i:]:
            return False
        i = s.index(0)
        s.pop(i)
        if 0 not in s[i:]:
            return False
        i = s.index(0)
        s.pop(i)
        if 7 not in s[i:]:
            return False
        return True

    
s = list(map(int, input().split()))
print(func(s))