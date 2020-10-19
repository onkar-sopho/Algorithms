'''
Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr. If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.
'''

def absSort(arr):
  return merge(arr)
  
	
def merge(arr): # arr = [2, -7, -2, -2, 0]
  if len(arr) == 1:
    #print(arr)
    return arr
  mid = len(arr) // 2  # 2
  left = merge(arr[:mid]) # 2, -7 
  right = merge(arr[mid:]) # -2, -2, 0 
  i = 0
  j = 0
  ans = []
  print(left, right, ans)
  while i < len(left) and j < len(right):
    if abs(left[i]) < abs(right[j]):
      ans.append(left[i])
      i += 1
    elif abs(left[i]) == abs(right[j]):
      if left[i] < right[j]:
        ans.append(left[i])
        i += 1
      else:
        ans.append(right[j])
        j += 1
    else:
      ans.append(right[j])
      j += 1
    print(ans)
    
      
  while i < len(left):
    ans.append(left[i])
    i += 1
    
  while j < len(right):
    ans.append(right[j])
    j += 1
    
  return ans
  
arr = [2, 0, 2] 
print(absSort(arr))#
