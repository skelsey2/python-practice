# 2
# Iterative Binary Search
#  done on Sorted Arrays, generally
#  2 pointers, one at the start and end
# Recursive

def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1        
        else:
            return mid
    return start


def binary_search_test1(arr, start, end, target):
    iter = 0
    while (start <= end):
        iter += 1
        mid = (start + end) - 1 // 2
        if(arr[mid] < target):
            start = mid + 1
        elif(arr[mid] > target):
            end = mid -1
        else:
            return mid, iter
    return -1, iter

def binary_itr2(arr, start, end, target):
    while (start <= end):
        mid = (start + end) // 2
        if(arr[mid] < target): # Reads - if middle of array smaller than target
            start = mid + 1 # cut off the smaller numbers by resetting the start number to mid +1
        elif(arr[mid] > target): # Reads - if middle of the array bigger than target
            end = mid -1    # cutt off the bigger numbers by resetting the start number to mid -1
        else:
            return mid
    return start


def binary_recur(arr, start, end, target):
    if end >= start:
        mid = start + end - 1 // 2
        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)
        elif arr[mid] > target:
            return binary_recur(arr, start, mid -1, target)
        else:
            return mid
    else:
        return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 5
result = binary_search_test1(arr, 0, len(arr)-1, target)

# result = binary_itr2(arr, 0, len(arr)-1, target)

if result != -1:
    print(" Element is present at index %d,%d" % result)
else:
    print("Element is not present in array")


