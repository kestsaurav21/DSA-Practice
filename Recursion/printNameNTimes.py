# Problem: Print your Name N times using recursion

def printName(i, n):
    if i > n:   # base case
        return
    print("Saurabh")  # print the name
    printName(i+1, n)  # recursive call


n = 5
i = 1
printName(i, n)   # just call the function, don't print its return
