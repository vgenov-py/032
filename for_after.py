import matplotlib.pyplot as plt
import time

times = 10000
counter = 0
result = 0
measurements_1 = []
measurements_2 = []

while counter < times:
    start = time.perf_counter()
    for number in range(1,counter):
        result += number
    finish = time.perf_counter()
    measurements_1.append(finish-start)
    counter += 50

    measurements_2.append(counter * (counter + 1) / 2)

print(measurements_1)
plt.plot(measurements_1)
plt.plot(measurements_2)

plt.show()