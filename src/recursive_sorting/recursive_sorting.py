# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0

    for i in range (0, len(merged_arr)):
        if len(arrA) > a and len(arrB) > b:
            if arrA[a] < arrB[b]:
                merged_arr[i] = arrA[a]
                a +=1  
            elif arrB[b] < arrA[a]:
                merged_arr[i] = arrB[b]
                b += 1
        elif a == len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b == len(arrB):
            merged_arr[i] = arrA[a]
            a += 1            
            
    return merged_arr


  


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) == 1:
        return arr  
    if len(arr) > 1:
        LHS = arr[0: len(arr)//2] 
        RHS = arr[len(arr)//2 :]
        return merge(merge_sort(LHS), merge_sort(RHS))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
