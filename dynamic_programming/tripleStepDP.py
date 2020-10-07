import time
def tripleStepDP(n):
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        counts = [1] * (n + 1)
        counts[2] = 2
        for i in range(3,n + 1):
            counts[i] = counts[i - 1] + counts[i - 2] + counts[i - 3]
        return counts[n]

start_time = time.time()
print("DP n = 1: " + str(tripleStepDP(1)))
print("DP n = 2: " + str(tripleStepDP(2)))
print("DP n = 3: " + str(tripleStepDP(3)))
print("DP n = 4: " + str(tripleStepDP(4)))
print("DP n = 5: " + str(tripleStepDP(5)))
print("DP n = 6: " + str(tripleStepDP(6)))
print("DP n = 30: " + str(tripleStepDP(30)))
print("DP n = 150: " + str(tripleStepDP(150)))
print("DP n = 300: " + str(tripleStepDP(300)))
print("DP n = 500: " + str(tripleStepDP(500)))
print("DP n = 1000: " + str(tripleStepDP(1000)))
print("DP n = 10000: " + str(tripleStepDP(10000)))
print("--- %s seconds ---" % (time.time() - start_time))