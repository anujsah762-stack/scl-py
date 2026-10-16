def hcf(a, b):
  if a > b:
    c = b
  else:
    c = a

  for i in range(c, 0, -1):
    if a % i == 0 and b % i == 0:
      h = i
      break 

  print("HCF of", a, "and", b, "is", h)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
hcf(x, y)