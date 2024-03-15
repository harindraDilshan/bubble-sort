def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# I changed this code. bubble_sort_3.py comming soon ...
arr = [12, 6, 7, 8, 10, 2, 9]

print(bubble_sort(arr))

# I love learn algorithm ...... 