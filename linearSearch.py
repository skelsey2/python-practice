# Linear Search Example
# find the index of the number 10
#       the algorithm searches for the number one at a time until it is found

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        

arr = [2, 5, 8, 9, 10, 16, 22]
target = 10

print(search(arr,target))
