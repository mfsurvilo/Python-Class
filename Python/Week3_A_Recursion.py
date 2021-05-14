# The repeated application to a smaller and smaller quantity

#Having a function call itself until a basecase exists

def factorial(n):
  if n<2:
    return 1
  return n * factorial(n-1)

  print(factorial(4)  )
