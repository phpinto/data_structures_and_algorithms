def are_all_unique(string):
    if len(string) == 0:
        return "This is an empty string"
    elif len(string) == 1:
        return True
    else:
        for i in range(len(string)-1):
            for j in range(i+1,len(string)):
                if string[j] == string[i]:
                    return False
        return True
        

print(are_all_unique("ajsk lwpd"))
print(are_all_unique("Victor Arthurzinho"))
print(are_all_unique("abc defghuj"))
print(are_all_unique("Mariliao Mariliao"))