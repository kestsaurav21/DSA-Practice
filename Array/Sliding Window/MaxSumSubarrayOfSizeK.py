# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

# Note: A subarray is a contiguous part of any given array.


class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        sum = 0
        sumOfSubArray = []
        n = len(arr)
        
        for i in range(k):
            sum += arr[i]
            
        
        for j in range(k, n):
            sumOfSubArray.append(sum)
            sum+=arr[j]
            sum-=arr[j-k]
        sumOfSubArray.append(sum)
        
        return max(sumOfSubArray)
        
        
