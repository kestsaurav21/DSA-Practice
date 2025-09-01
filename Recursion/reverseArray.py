
# def reverseArray(arr, n):

#     ans = [0] * n
#     for i in range(n-1, -1, -1):
#         ans[n-1-i] = arr[i]


#     print("The reversed array is:- ")
#     for i in range(n):
#         print(ans[i], end=" ")
#     print()

def reverseArray(arr, left, right):

    if left>=right:
        return
  
    arr[left], arr[right] = arr[right], arr[left]
        
    reverseArray(arr, left+1, right-1)

    
if __name__ == "__main__":
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

    if len(arr) != n:
        print("Error: Number of elements entered does not match the length.")

    # reverseArray(arr, n)
    reverseArray(arr, 0, n-1)

    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()