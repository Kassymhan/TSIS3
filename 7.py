def has_33(nums):
    s = 0
    spl = nums.split()
    for i in range(0, len(spl) - 1, 1):
        if int(spl[i]) == 3 == int(spl[i + 1]):
          s = s + 1
        
        if s > 0:
           return True
    return False
        

nums = input()
print(has_33(nums))