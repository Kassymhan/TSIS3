def func(s):
    t = s
    if t == s[::-1]:
        print("YES")
    else:
        print("NO")
    

s = input()
func(s)