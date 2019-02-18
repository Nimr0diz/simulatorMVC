
CONSTANTS = {
  'B': 1
}



def time_function(t):
  if t < 0:
    return 0
  else:
    return (t ** CONSTANT_B())

def price(t, p):
  return p * time_function(t)

