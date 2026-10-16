def check(n):
  c = 0
  for i in range(1, n + 1):
    if n % i == 0:
      c = c + 1
  return c


x = int(input("Enter a number: "))
d = check(x)

if d == 1:
  print(x, "is neither prime nor composite.")
elif d == 2:
  print(x, "is a prime number.")
else:
  print(x, "is a composite number.")