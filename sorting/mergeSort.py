# 5/5/2023 - did in IK platform, took an hour
#  hardest part was understanding "arr[start:end+1] = aux"
#   trying to copy the aux array into the main arr without new assignment, 
#   I didn't think of use a range within the array although the video stated explicitly

def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    helper(arr, 0, len(arr)-1)
    
       
    return arr

def helper(arr, start, end):
    if(start >= end):
        return
    
    mid = (start + end) // 2
    helper(arr, start, mid)
    helper(arr, mid+1, end)
    
    i = start
    j = mid + 1
    aux = []
    while ( i <= mid and j <= end):
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j <= end:
        aux.append(arr[j])
        j += 1
    arr[start:end+1] = aux
    
    