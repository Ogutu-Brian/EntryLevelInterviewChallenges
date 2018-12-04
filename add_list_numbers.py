###################################################################################
# Question: Given a list of numbers and a number K, return whether any two numbers
# from the list add up to k
# Bonus: Can you do this in one pass?
# This is a simple google type Question
###################################################################################
from typing import List


def check_sum(sample_list: List, k: int) -> bool:
  """
  Checks if the sum of any two numbers in the list result into a given value
  """
  counter = 0
  for item in sample_list:
    for val in sample_list[counter:]:
      if (item+val) == k:
        return True
    counter += 1
  return False
