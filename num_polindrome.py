def polindrome(num):
    temp = num
    reverse = 0
    
    while num>0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //=10
    return temp == reverse
        
try:
    num = int(input("Enter a number : "))
    if polindrome(num):
        print("number is a polindrome")
    else:
        print("Number is not a polindrome")
except:
    print("Invalid input")