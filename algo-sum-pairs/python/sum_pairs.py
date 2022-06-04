import re


def sum_pairs(arr, sum):
  results = []

  # Loop through each pair combo
  for i in arr:
    for j in arr:
      # Ensures no duplicate pair combos
      if j > i:
        # If sum of pair combo == sum, append pair to results[]
        if (i + j) == sum:
          results.append([i,j])
  
  if results == []:
    return 'Unable to find pairs'
  
  return results
