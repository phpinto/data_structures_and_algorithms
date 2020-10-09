def insert_max_5(N):
    # convert N to a string:
    str_N = str(N)
    if N >= 0:
        for i in range(0, len(str_N)):
            if '5' > str_N[i]:
                return int(str_N[:i] + '5' + str_N[i:])
        return int('5' + str_N)
    else:
        for i in range(1, len(str_N)):
            if '5' > str_N[-i]:
                return int(str_N[:i] + '5' + str_N[i:])
        return int('-' + '5' + str_N[1:])

print(insert_max_5(9999))
print(insert_max_5(268))
print(insert_max_5(670))
print(insert_max_5(0))
print(insert_max_5(-999))