# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  low = 0
  high = len(arr)-1

  if len(arr) == 0:
    return -1 # array empty
    
  # # TO-DO: add missing code
  while low <= high:
      middle = (low+high)//2
      if arr[middle] > target:
        high = middle-1
      elif arr[middle] < target:
        low = middle+1
      else:
        return middle  
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  elif arr[middle] == target:
    return middle  
  # TO-DO: add missing if/else statements, recursive calls
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle-1)
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle+1, high)
  else:
    return -1 

#Question for Pascal: I managed to get this recursion function working, but I don't fully understand how the function knows that low is low and high is high without declaring their values?  
