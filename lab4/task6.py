import time


def build_with_loop(numbers):
  result = []
  for x in numbers:
    if x % 2 == 0:
      result.append(x * x)
  return result


def build_with_comprehension(numbers):
  return [x * x for x in numbers if x % 2 == 0]


sizes = [10_000, 100_000, 1_000_000]
runs = 7

for size in sizes:
  data = list(range(size))
  loop_times = []
  comp_times = []

  for _ in range(runs):
    start = time.time()
    build_with_loop(data)
    loop_times.append((time.time() - start) * 1000)

    start = time.time()
    build_with_comprehension(data)
    comp_times.append((time.time() - start) * 1000)

  avg_loop = sum(loop_times) / len(loop_times)
  avg_comp = sum(comp_times) / len(comp_times)

  print(f"Размер: {size}")
  print(f"Цикл : {[round(t, 4) for t in loop_times]} ")
  print(f"Comprehension : {[round(t, 4) for t in comp_times]}  \n")