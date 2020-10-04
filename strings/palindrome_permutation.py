def isPalindromePermutation(perm_str):
    char_counts = {}
    real_length = 0
    for char in perm_str.lower():
        if char == ' ':
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
        real_length += 1
    odd_count = 0
    max_odd_count = 0 if ((real_length % 2) == 0) else 1
    for char in char_counts:
        if (char_counts[char] % 2 == 1):
            odd_count += 1
            if odd_count > max_odd_count:
                return False
    return True

print(isPalindromePermutation('Tact Coa'))
print(isPalindromePermutation('Abacate Verde'))
print(isPalindromePermutation('Arara'))
print(isPalindromePermutation('Arara Azul'))
print(isPalindromePermutation('A nut for a jar of tuna'))
print(isPalindromePermutation('natua ja r fo A nut rof'))