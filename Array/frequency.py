#############################################################
# Find the Frequency(occurrence of an integer in the array) #
#############################################################

def findFrequency(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(findFrequency(arr, n, x))