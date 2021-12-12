#######################
# Find a peak element #
#######################

# An array element is a peak if it is NOT smaller than its neighbours. 
# For corner elements, we need to consider only one neighbour. 

# find the peak element in the array
def findPeak(arr, n):
    
    # first or last element is peak element
    if (n == 1) :
        return 0
    if (arr[0] > arr[1]) :
        return 1
    if (arr[n - 1] > arr[n - 2]) :
        return 1

    # check for every other element
    for i in range(1, n - 1) :
        # check if the neighbours are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return 1
    return 0


n = int(input())
arr = list(map(int,input().split()))
print(findPeak(arr,n))