def is_larger(str1,str2):
    if len(str1) > len(str2):
        return True
    elif len(str1) < len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        if str1[i] > str2[i]:
            return True
        else:
            return False
    return False

print(is_larger("112","111"))
print(is_larger("525","1111"))
print(is_larger("456456","5555"))
print(is_larger("45","4546"))
print(is_larger("458","321"))
print(is_larger("232","233"))
print(is_larger("11","0"))
print(is_larger("1","1"))
print(is_larger("45629137","45629137"))