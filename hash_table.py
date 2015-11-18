import random

def hash_table(count_list):
    dictionary = {}
    for item in count_list:
        dictionary.setdefault(item, 0)
        dictionary[item] +=1
    return dictionary


list_count = [random.randint(1, 100) for x in range(10000)]

print hash_table(list_count)
