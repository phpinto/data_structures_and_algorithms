def stringCompression(uncomporessed):
    comp_list = []
    counter = 0

    for i in range(len(uncomporessed)):
        counter += 1
        if (i + 1) >= len(uncomporessed) or uncomporessed[i] != uncomporessed[i + 1]:
            comp_list.append(uncomporessed[i])
            comp_list.append(str(counter))
            counter = 0

    return ''.join(comp_list) if len(comp_list) < len(uncomporessed) else uncomporessed


print(stringCompression('aabcccccaaa'))
print(stringCompression('aaaaaaaaaaaaaaaaaaaaaa'))
print(stringCompression('aaaaaaahhhiiiiiissjjjjjjkkkkllslsmdj'))
print(stringCompression('ahdjskalsldksjabsbwbiji'))
print(stringCompression('eu nasci a dez mil anos atras'))