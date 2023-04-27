# Iterative Binary Search
#  done on Sorted Arrays, generally
#  2 pointers, one at the start and end

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

arr = [2,5, 8, 10, 16, 22, 25]
target = 10

result = binary_recur(arr, 0, len(arr)-1, target)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")


