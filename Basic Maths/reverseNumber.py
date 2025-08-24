def reverseNumber(num):
    reverse = 0

    while num > 0:
        digit = num%10
        reverse = reverse*10 + digit
        num = num//10

    return reverse







num = int(input("Enter the number: "))
print("Reverse Number is: ", reverseNumber(num))