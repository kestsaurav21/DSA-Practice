

# def gcdNumber(num1, num2):
#     mini = min(num1, num2)
#     gcd = 1

#     for i in range(1, mini):
#         if (num1 % i == 0 and num2 % i == 0):
#             gcd = max(gcd, i)

#     return gcd



# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print("GCD is: ", gcdNumber(num1, num2))



# Better Approach
# def gcdNumber(num1, num2):
#     mini = min(num1, num2)
    
#     for i in range(mini, 0, -1):
#         if (num1 % i == 0 and num2 % i == 0):
#             return i
#     return 1

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print("GCD is: ", gcdNumber(num1, num2))

# Euclidean Algorithm - It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.

def gcdNumber(num1, num2):
    while num1>0 and num2>0:
        if num1>num2:
            num1= num1%num2
        else:
            num2= num2%num1

    if num1 == 0: 
        return num2
    else:
        return num1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("GCD is: ", gcdNumber(num1, num2))