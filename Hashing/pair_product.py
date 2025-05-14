def pair_product(numbers, target_product):
  previous = set()

  for idx, number in enumerate(numbers):
    complement = target_product / number
    if target_product % number != 0:
      continue
    
    if complement in previous:
      for idx2, num2 in enumerate(numbers):
        if num2 == complement:
          return idx, idx2
        
    else:
      previous.add(number)

  return idx, idx2