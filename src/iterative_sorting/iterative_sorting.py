# TO-DO: Complete the selection_sort() function below
test = [3, 2, 1, 6, 4, 9, 0]


def selection_sort(arr):
    # loop through n-1 elements

    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
          
    return arr


# print(selection_sort(test), 'selection')


# # TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
        for i in range(0, len(arr)-1):
            swapped = False
            for j in range(0, len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped == True:
                break  

        return arr


print(bubble_sort(test), 'bubble')
#Question for Pascal - I did try to run the bubble algorithm without the nested loop, but ran into problems trying to get it to repeat enough times to work. Is there a way to run it that way or is it only possible with a nested loop? 

# Also, I was trying to find a way of optmising the code to make it stop if there had been now swaps. I found lots of pseudocode online telling me to put a boolean of false within the first loop and a boolean of true at the end of the second, but my brain doesn't fully understand exactly why line 28 works.


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
    #I was about to try this one but the 'maximum=-1' argument really threw me. I'm not sure what that means. I was expecting to pass in two arrays(original array and results array), and maybe the range of the numbers? I'm not really sure yet how to implement it.

        



        

#     return arr
