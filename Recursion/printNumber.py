# Problem: Print from 1 to N using Recursion

# def printN(i, n):

#     if i > n: 
#         return
#     print(i)
#     printN(i+1, n)


# n = 5
# i = 1
# printN(i, n)

# Problem: Print from N to 1 using Recursion



def printN(i, n):

    if n < i: 
        return
    print(n)
    printN(i, n-1)



n = 5
i = 1
printN(i, n)