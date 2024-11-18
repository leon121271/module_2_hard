result = ""
for n in range(3, 21):
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += str(i) + str(j)
    print(f"{n} - {result}")
    result = ""