# sliding window practice

# for an array of size n, find the largest sum of a substring of size m

def findLargestSub(arr, m):
    largest = 0
    for i in range(len(arr) - m + 1):
        sum = 0
        for j in range(m):
            sum += arr[i + j]
            
        if sum > largest:
            largest = sum

    return largest
            
arr = [1, 2, -2, 5, 1, 9, 2, -5, 7, 12]
m = 3

print(findLargestSub(arr, m))

# Given an array of integers, find the subarrays which add up to a given number

def findGivenSum(arr, n):
    indices = []
    
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr) - i):
            if j == 0 and arr[i + j] == 0: 
                break
            sum += arr[i + j]
            if sum == n:
                indices.append((i, j+1))
                break
            if sum > n:
                break
    return indices
    
arr = [-9, 1, 2, 0, 6, 0, 0, 0, 5, 4, 9, 2, 1, 8, -1, 2, 2, 2, 2, 1]
# the -9 at index 0 renders this algorithm innacurate
n = 9

print("Wrong find given :(")
print(findGivenSum(arr, n))

# try again
# Given an array of integers, find the subarrays which add up to a given number

def findGivenSum2(arr, n):
    indices = []
    toAdd = -1*min(arr)
    print("toAdd: " + str(toAdd))
    newN = n + 4*toAdd  #TODO: try to improve this somehow, the newN needs to be equal to the length of the correct subarray time toAdd
    print("newN: " + str(newN))
    
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr) - i):
            if j == 0 and arr[i + j] + toAdd == 0: 
                break
            sum += (arr[i + j] + toAdd)
            if sum == newN:
                indices.append((i, j+1))
                break
            if sum > newN:
                break
    return indices
    
print("New find given!")
print(findGivenSum2(arr, n))
