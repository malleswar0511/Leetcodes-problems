def right_shift(num,n):
    if num<=0:
        return 0
    elif num ==1:
        return 1
    else:
        shift_data = num >> n
        return shift_data

n1 = 30;n2=2
print(right_shift(n1,n2))
    