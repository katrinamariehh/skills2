# Write a function that takes an iterable (something you can loop through, 
# ie: string, list, or tuple) and produces a dictionary with all distinct 
# elements as the keys, and the number of each element as the value
def count_unique(some_iterable):
    # create a dictionary
    unique_dict = {}
    # iterate through the iterable
    # if the item is in the dictionary
    for i in range(len(some_iterable)):
        if unique_dict.get(some_iterable[i]):
            unique_dict[some_iterable[i]] += 1
            # add 1 to the value associated with that key
        else:
            # otherwise add it as a new key and set the value to 1
            unique_dict[some_iterable[i]] = 1
    
    return unique_dict

# Given two lists, (without using the keyword 'in' or the method '.index()') 
# return a list of all common items shared between both lists
def common_items(list1, list2):
    # for each item in list 1
    in_both = []
    for i in list1:
    # compare to each item in list 2
        for j in list2:
            if j == i:
                in_both.append(i)
    return in_both
    # and add to in_both if it comes upon an equivalent value in list 2


# Given two lists, (without using the keyword 'in' or the method 'index') 
# return a list of all common items shared between both lists. This time, 
# use a dictionary as part of your solution.
def common_items2(list1, list2):
    # create a dictionary with the unique items of each list
    list_1_dict = count_unique(list1)
    list_2_dict = count_unique(list2)
    # generate the list of keys (the unique values) in the lists
    list_1_keys = list_1_dict.keys()
    list_2_keys = list_2_dict.keys()
    # push those into count_unique together
    both_dict = count_unique(list_1_keys + list_2_keys)
    print both_dict
    items = []
    # pull out keys with associated with the value 2
    for key, value in both_dict.iteritems():
        if value == 2:
            items.append(key)
    return items

