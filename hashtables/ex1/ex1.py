#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)
    for weight in weights:
        first_index = hash_table_retrieve(ht, weight)
        if weight == limit - weight:
            hash_table_remove(ht, weight)
        second_index = hash_table_retrieve(ht, limit - weight)
        if second_index is not None:
            if first_index > second_index:
                return (first_index, second_index)
            else:
                return (second_index, first_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
