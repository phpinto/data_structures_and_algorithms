def is_palindrome(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            j = len(str1) - i - 1
            if str1[i] != str2[j]:
                return False
        return True

print(is_palindrome("o rato roeu", "ate logo"))
print(is_palindrome("roma", "amor"))
print(is_palindrome("arara catu", "utac arara"))
print(is_palindrome("abacaxi", "ixacaba"))
print(is_palindrome("bom dia america", "america dia bom"))