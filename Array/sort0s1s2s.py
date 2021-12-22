#################################
# Sort an array of 0s 1s and 2s #
#################################

'''
# Approach 1
def sort012(arr, n):
    count0 = count1 = count2 = 0
    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        
    for i in range(count0):
        arr[i] = 0
    
    for i in range(count0, (count0 + count1)):
        arr[i] = 1
    
    for i in range((count0 + count1), n):
        arr[i] = 2
    
    return


arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
sort012(arr, len(arr))
print(arr)
'''

'''
# Approach 2
def sort012(arr):
    sort = []
    index = 0
    for i in arr:
        if i == 2:
            sort.append(i)
        elif i == 1:
            sort.insert(index, i)
            index += 1
        elif i == 0:
            sort.insert(0, i)
            index += 1
    
    print(sort)


arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
sort012(arr)
'''

# Approach 3
def sort012(arr, n):
    low = 0
    high = n - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1
        
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(arr, len(arr))
print(arr)