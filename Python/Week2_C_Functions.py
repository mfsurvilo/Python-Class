# Functions
def greeting(name):  # parameters get passed in
  print("Welcome, " + name)  #body of the function
  a=4
  return a


def TwoValueReturn():
    a = 2
    b = 4
    return a, b

d, e = TwoValueReturn

print(str(d) + str(e))
