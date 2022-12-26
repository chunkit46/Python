def create_pattern(n):
  result = []
  current = [1]
  result.append(current)
  for i in range(n - 1):
    next = []
    for j in range(len(current)):
      next.append(current[j] + current[j - 1])
    next.append(current[-1] + len(current))
    current = next
    result.append(current)
  return result

print(create_pattern(5))