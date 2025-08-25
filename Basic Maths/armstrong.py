
def checkArmstrong(num):
    num1 = str(num)
    k = len(num1)
    sum = 0
    n = num


    while n>0:
        digit = n%10
        sum += digit**k
        n = n//10

    if sum == num:
        return "Armstrong"
    
    else:
         return "Not a Armstrong"



num = int(input("Enter the number: "))
print(checkArmstrong(num))