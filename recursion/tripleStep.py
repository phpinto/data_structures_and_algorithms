import time

def tripleStepRec(n):
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return tripleStepRec(n - 1) + tripleStepRec(n - 2) + tripleStepRec(n - 3)

def tripleStepMem(n, mem_table = {}):
        
        if n in mem_table:
            return mem_table[n]
        if n == 0 or n == 1:
            count = 1
        elif n == 2:
            count = 2
        else:
            count = tripleStepMem(n - 1, mem_table) + tripleStepMem(n - 2, mem_table) + tripleStepMem(n - 3, mem_table)
            
        mem_table[n] = count
        return count
start_time = time.time()
print("Recursive n = 1: " + str(tripleStepRec(1)))
print("Recursive n = 2: " + str(tripleStepRec(2)))
print("Recursive n = 3: " + str(tripleStepRec(3)))
print("Recursive n = 4: " + str(tripleStepRec(4)))
print("Recursive n = 5: " + str(tripleStepRec(5)))
print("Recursive n = 6: " + str(tripleStepRec(6)))
print("Recursive n = 30: " + str(tripleStepRec(30)))
print("Recursive n = 35: " + str(tripleStepRec(35)))
print("--- %s seconds ---" % (time.time() - start_time))

print()

start_time = time.time()
print("Memoized n = 1: " + str(tripleStepMem(1)))
print("Memoized n = 2: " + str(tripleStepMem(2)))
print("Memoized n = 3: " + str(tripleStepMem(3)))
print("Memoized n = 4: " + str(tripleStepMem(4)))
print("Memoized n = 5: " + str(tripleStepMem(5)))
print("Memoized n = 6: " + str(tripleStepMem(6)))
print("Memoized n = 30: " + str(tripleStepMem(30)))
print("Memoized n = 150: " + str(tripleStepMem(150)))
print("Memoized n = 300: " + str(tripleStepMem(300)))
print("Memoized n = 300: " + str(tripleStepMem(500)))
print("Memoized n = 1000: " + str(tripleStepMem(1000)))
print("--- %s seconds ---" % (time.time() - start_time))