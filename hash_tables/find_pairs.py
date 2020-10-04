def find_pairs(nums):
    hash_table = set()
    for num in nums:
        if (10 - num) in hash_table:
            print("(" + str(10 - num) + "," + str(num) + ")")
            return
        elif num not in hash_table:
            hash_table.add(num)
    print("There is no pair that adds up to 10.")

find_pairs([3,4,1,2,9])
find_pairs([3,4,2,2,9,13,44])
find_pairs([5,4,2,5,9,13,44])
find_pairs([3,4,2,2,9,13,44,-3])
find_pairs([3,4,20,2,9,131,44,-3,0,0,2,-10])
find_pairs([5,4,2,9,13,44])