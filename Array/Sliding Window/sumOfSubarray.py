# Given an integer array ‘Arr[N]’. Print the individual sum of all the subarrays of length ‘k’.

def sumOfSubArray(arr, k):
    n = len(arr)
    newArr = []
    

    for i in range(n-k+1):
        sum=0
        for j in range(i, i+k):
            sum += arr[j]
        newArr.append(sum)
    return newArr    

arr = [4,7,3,1,5,2]
k = 3
print(sumOfSubArray(arr, k))