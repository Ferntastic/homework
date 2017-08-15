in_arr = [3, 5, 9, 7, 24, 42, 13, 19, 2]

def swap (arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
def bubble_sort(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[ + 1]:
                swap(arr, i, i + 1)
                done = False
        
bubble_sort(in_arr)

print "array is", in_arr
