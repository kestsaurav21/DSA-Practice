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

# Optimized - using sliding window

def subArrayOfK(arr, k):
    n = len(arr)
    sum=0
    for i in range(k):
        sum+=arr[i]

    for j in range(k,n):
        print(sum)
        sum+=arr[j]
        sum-=arr[j-k]
    print(sum)

arr = [4,7,3,1,5,2]
k = 3
subArrayOfK(arr, k)
