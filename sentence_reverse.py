'''
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.
'''


def reverse_words(arr):
  if len(arr) == arr.count(' '):
    return arr
  temp1 = []
  for i in range(len(arr)):
    if arr[i] == ' ':
      temp1.append(i)
  counti = arr.count(' ')
  arr = ''.join(arr)
  arr = arr.split()
  for i in range(len(arr)//2):
      temp = arr[i]
      arr[i] = arr[len(arr)-i-1]
      arr[len(arr)-i-1] = temp
  arr = list(' '.join(arr))
  #print(temp1)
  countf = arr.count(' ')
  if counti != countf:
    for i in temp1:
      if arr[i] != ' ':
        #print(arr[:i] + [' '] + arr[i:])
        arr = arr[:i] + [' '] + arr[i:]
  return arr

arr = ["a"," "," ","b"]
print(reverse_words(arr))


#def help


'''
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', i = 7
                'm', 'a', 'k', 'e', 's', '  ', j = 13
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

arr1 = ['p', 'e', 'r', 'f', 'e', 'c', 't']
arr1 = ['m', 'a', 'k', 'e', 's', '  '].extend(arr1)
['m', 'a', 'k', 'e', 's', '  ','p', 'e', 'r', 'f', 'e', 'c', 't']
'''
