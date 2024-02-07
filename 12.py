def hist(s):
    s = s.split()
    for x in s:
        t = int(x)
        
        print("*" * t, end = " ")
        
        print()

s = input()
hist(s)