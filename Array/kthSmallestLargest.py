####################################
# Kth smallest and largest element #
####################################

def kthSmallest(arr, n, k):
    arr.sort()
    return arr[k-1]

def kthLargest(arr, n, k):
    arr.sort()
    return arr[n-k]

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(kthSmallest(arr, n, k))
print(kthLargest(arr, n, k))