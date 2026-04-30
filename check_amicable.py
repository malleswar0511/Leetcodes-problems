def check_amicable(num):
    count = 0
    for n in range(1,num):
        if num%n==0:
            count += n
    return count
            
        

def check_amicable_numbers(n1,n2):
    if check_amicable(n1)==n2 and check_amicable(n2)==n1:
        print(f"{n1} and {n2} are amicables")
    else:
        print(f"{n1} and {n2} are not amicables")
        
n1 = 220
n2 = 284  
check_amicable_numbers(n1,n2)