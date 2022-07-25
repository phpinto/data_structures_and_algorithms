def get_counts(input_str):
    count_dict = {}
    for i in input_str:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def anagram_indexes(A, B):
    idx = []
    if len(A) <= len(B):
        set_A = get_counts(A)
        for i in range(len(B) - len(A) + 1):
            if get_counts(B[i:i+len(A)]) == set_A:
                idx.append(i)
    elif len(B) < len(A):
        set_B = get_counts(B)
        for i in range(len(A) - len(B) + 1):
            if get_counts(A[i:i+len(B)]) == set_B:
                idx.append(i)
    return idx

print(anagram_indexes('abcdcbac','abc'))
print(anagram_indexes('abcdcbac','abccacdb'))
print(anagram_indexes('abcdcbac','abccxcdb'))
print(anagram_indexes('hello hole loh hol helololhoholo','hol'))
print(anagram_indexes('hello hole leh hol helololhoholo','hel'))