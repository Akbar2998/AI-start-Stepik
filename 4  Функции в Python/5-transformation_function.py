def Set(func):
  global transformation_func
  transformation_func = func

def Compute(string):
  return transformation_func(string)
