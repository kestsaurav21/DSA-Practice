
# def palindrome(num):
#     reverse = 0
#     n = num

#     while num > 0:
#         digit = num%10
#         reverse = reverse*10 + digit
#         num = num//10

#     if reverse == n: 
#         return "Palindrome"
#     return "Not a Palindrome"


def palindrome(num):
    num = str(num)
    left = 0
    right= len(num)-1

    while left<right:
        if num[left] == num[right]:
            left+=1
            right-=1
        else: 
            return "Not a palindrome"

    return "Palindrome"


num = int(input("Enter the number: "))
print(palindrome(num))