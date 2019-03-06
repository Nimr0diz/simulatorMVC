from model.utils.constants import CONSTANTS

def time_function(t):
  if t < 0:
    return 0
  else:
    return (t ** CONSTANTS['B'])

def price(t, p):
  return p * time_function(t)

