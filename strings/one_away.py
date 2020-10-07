from collections import defaultdict 
  
def oneAway(str1, str2):
    diff_count = 0
    if abs(len(str1) - len(str2)) > 1:
        return False
    elif len(str1) == len(str2):
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                diff_count += 1
        if diff_count > 1:
            return False
        else:
            return True
    else:
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                diff_count += 1
        if diff_count == 0:
            return True
        elif diff_count == 1:
            if len(str1) == len(str2) or str1[-1] == str2[-1]:
                return True
        else:
            return False

print(oneAway('pale','ple'))
print(oneAway('pales','pale'))
print(oneAway('pale','bale'))
print(oneAway('pale','bake'))
print(oneAway('test','test'))
print(oneAway('test','testtest'))