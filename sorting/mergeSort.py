# Merge Sort - 5/1/2023
#  Brute force - Took me a minute to understand as it looked like it was only working with the minimum value
#                       then realizing the minimum value gets removed each iteration
#  Merge Sort has a time complexity of O(n log n), which makes it an efficient sorting algorithm for large arrays.
#  https://www.youtube.com/watch?v=fW_OS3LGB9Q&ab_channel=freeCodeCamp.org

# Brute force - slow, basic example
def bruteforce_mergesort():
    A = [-5, 25, 5, 0, 23, -6, 23, 67]
    C = []
    while A:
        minimum = A[0]
        for x in A:
            if x < minimum:
                minimum = x
        C.append(minimum)
        A.remove(minimum)
    print(C)
# bruteforce_mergesort() # Invoke the method to print Array sorted  


# Merging two pre-sorted arrays into 3rd array 'C' 
def mergingSorted(left, right):
    C = []
    while min(len(left), len(right) > 0 ):
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C

left = [2, 5, 6, 10]
right = [3, 4, 12, 20]
# print( mergingSorted(left, right))


# 3rd Example using Chat GPT without having pre-sorted arrays
def merge_sort_byGPT(arr):
    # Base case: if the input array has only one element, it's already sorted
    if len(arr) == 1:
        return arr
    
    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the left and right halves
    sorted_left = merge_sort_byGPT(left_half)
    sorted_right = merge_sort_byGPT(right_half)
    
    # Merge the sorted halves back together
    return merge_byGPT(sorted_left, sorted_right)
    
def merge_byGPT(left, right):
    result = []
    i = j = 0
    
    # Compare the elements of the two arrays, and add the smaller one to the result array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements from the left or right arrays to the result
    result += left[i:]
    result += right[j:]
    
    return result

# Chat GPT code example 
arr = [3, 6, 2, 8, 1, 9, 4, 7, 5]
sorted_arr = merge_sort_byGPT(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
