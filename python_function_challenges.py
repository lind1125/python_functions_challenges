
# Challenge 1
def sum_to(n):
  arr = []
  for i in range(1, n+1):
    arr.append(i)
    result = sum(arr)
  print('Challenge 1:', result)

sum_to(6) # returns 21
sum_to(10) # returns 55

# Challenge 2 Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers.

def largest(arr):
  result = max(arr)
  print('Challenge 2:', result)

largest([10, 4, 2, 231, 91, 54])  # returns 231
largest([1,2,3,4,0])  # returns 4

# Challenge 3 Write a function named occurrences() that takes two string parameters and counts the number of occurrances of the second string inside the first string.

# Didn't quite get there. Looking at the solution, looks like I was on the right track though.
def occurrences(str, substr):
  arr = []   
  if substr in str:
      arr.append(substr)
  print(arr)
  result = len(arr)
  print('Challenge 3:', result)

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0


# Wasn't able to get to Challenge 4. Will read up on *args