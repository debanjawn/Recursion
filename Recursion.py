def test(x):
  print ((' ' * x)+str(x))
  if x > 0:
    test(x-1) 
    test(x-1)
  


test(3)