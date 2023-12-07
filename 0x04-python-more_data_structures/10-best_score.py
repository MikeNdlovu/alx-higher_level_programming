#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    if a_dictionary is None:
        return None

    for i in a_dictionary:
        num = int(a_dictionary[i])
        if highest < num:
            highest = a_dictionary[i]
            store = i
    return store
