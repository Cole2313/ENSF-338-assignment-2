

times = []
indexs = []
for i in range(36):
    times.append(timeit.timeit(lambda: func(i), number = 1))
    indexs.append(i)
print(times)
print(indexs)

plt.title("Time to calculate numbers 0-35 in the fibonacci sequence")
plt.plot(indexs, times)
plt.xlabel("fibonacci index")
plt.ylabel("Time (s)")
plt.show()
