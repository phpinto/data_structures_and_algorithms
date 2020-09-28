def countdown(num):
    if (num == 0):
        print("Done!")
        return
    else:
        print(num)
        return countdown(num - 1)

def power(num, pwr):
    if (pwr == 0):
        return 1
    else:
        return num * power(num, pwr - 1)

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)