# Problem: Print from 1 to N using Recursion

def printN(i, n):

    if i > n: 
        return
    print(i)
    printN(i+1, n)


n = 5
i = 1
printN(i, n)