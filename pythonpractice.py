print('hello worldz')

# Linear Search
"""
what is the best algorithm for sorted large arrays? Chat GPT
For sorting large arrays, the most efficient algorithms are usually those with a time complexity of O(n log n). 
    There are several algorithms that fall into this category, including Merge Sort, Quick Sort, and Heap Sort. 
However, when dealing with already sorted or nearly sorted large arrays, the best algorithm to use is typically 
    Insertion Sort. This is because Insertion Sort has a time complexity of O(n) for nearly sorted or already 
    sorted arrays, which makes it significantly faster than algorithms with O(n log n) time complexity.
So, in summary, if you are dealing with a large array that is already sorted or nearly sorted, Insertion Sort 
    is likely to be the best choice. Otherwise, if the array is unsorted or has no specific pattern, Merge Sort,
    Quick Sort, or Heap Sort are good options.

Search
-Binary Search
    Iterative version needs:
        Array must be sorted
        Loop start <= end
        use (start + end -1) // 2 to get the mid
        while loop, incrementing or decrementing the mid variable each iteration
        use blocks of ifs - mid >, <, = target 
            if target is smaller than mid,  end = -1 to mid  (going to the left of the arraay, cut off the bigger numbers)
                target < mid aka mid > target ->   end = -1
            if target is bigger than mid, start = +1 to mid  (going to the right of the array, cut off the smaller numbers)
                target > mid aka mid < target -> start = +1
-Depth-first Search/traversal 


Structures
-Linked Link
-
Sorts
-Insertion Sort
-Bubble Sort
"""