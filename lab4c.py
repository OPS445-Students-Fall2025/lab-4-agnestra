#!/usr/bin/env python3

'''
Lab4c: Dictionaries
'''

#Author: Agnestra Mahat
#AuthorID: 128939238

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):        # function that acccepts two lists as arguments
    my_dict = {}                            #creates an empty dictionary
    index = 0                               #variable for indexes of lists
    # while loops  compares the length of lists is smaller than the index for the program to run
    while index < len(keys) and index < len(values):
    #assigns the values and keys that are in the same index in the lists as key:pair and add it to the dictionary        
     my_dict[keys[index]]= values[index]
     index = index + 1                   # increse the index to move to the next values in the provided lists
    return my_dict                                                
    

def shared_values(dict1, dict2):
    set1 = set(dict1.values())      #converts dict1 values to set1
    set2 = set(dict2.values())      #converts dict2 values to set2
    return set1 & set2              #returns the values that intersect in set1 and set2


# Main Program

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)