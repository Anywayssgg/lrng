sqrs1 = []
for number in range(101):
  if number % 2 == 0:
    sqrs1.append(number**2)

sqrs2 = [number**2 for number in range(101) if number % 2 == 0]

print(sqrs1 == sqrs2)