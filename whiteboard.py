# You get an array of numbers, return the sum of all of the positives ones.
# Note: if there is nothing to sum, the sum is default to 0.
# EXAMPLES:
# positive_sum([1,2,3,4,5]) --> 15
# positive_sum([1,-2,3,4,5]) --> 13
# positive_sum([-1,2,3,4,-5]) --> 9

def sumOfPositives(arrayOfNums):
  sum = 0
  
  for number in arrayOfNums:
    if number > 0:
      sum += number

  print(sum)
  return sum

sumOfPositives([-1,2,3,4,-5])