import time

n = 10000000
result = 0
rango = range(1,n +1)
s_1 = time.perf_counter()

# BIG O NOTATION O(n)

for num in rango:   # O(n * 3) --> O(n**2)
    result += num

f_1 = time.perf_counter()

# print(f"result 1: {f_1 - s_1}")

s_2 = time.perf_counter()

result_2 = n * (n + 1) / 2 # O(4)  ---> O(1)

f_2 = time.perf_counter()
# print(f"result 2: {f_2 - s_2}")
