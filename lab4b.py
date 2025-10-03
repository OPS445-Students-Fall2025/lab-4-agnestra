#!/usr/bin/env python3

''' Lab4b: List Manipulation '''

# Author: Agnestra Mahat
# Author ID: 128939238
def join_lists(l1, l2):
    s1= set(l1)             #list1 to set1
    s2= set(l2)             #list2 to set2
    return list(s1 | s2)        #joins set1 and set2 using set union and returns it as list

def match_lists(l1, l2):
    s1= set(l1)             #list1 to set1
    s2= set(l2)             #list2 to set2
    return list(s1 & s2)   #matches set1 and set2 using set intersection and returns it as list
# match_lists will return a list that contains all values found in both l1 and l2



def diff_lists(l1, l2):
    s1= set(l1)             #list1 to set1
    s2= set(l2)             #list2 to set2
    return list(s1 ^ s2)    #find different values within a list and returns it as list
    # diff_lists will return a list that contains all different values, which are not shared between the lists

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))