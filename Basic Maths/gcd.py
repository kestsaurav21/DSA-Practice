def gcdNumber(num1, num2):
    mini = min(num1, num2)
    gcd = 1

    for i in range(1, mini):
        if (num1 % i == 0 and num2 % i == 0):
            gcd = max(gcd, i)

    return gcd



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("GCD is: ", gcdNumber(num1, num2))