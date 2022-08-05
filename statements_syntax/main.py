from array import array
from random import randint


def task_1(original_array, value):
    """
    check if value exists in array
    """
    return value in original_array


def task_2(original_array):
    """
    chrck if 7 appears as first or last element of array
    """
    if len(original_array) <= 1:
        return False
    return original_array[0] == 7 or original_array[-1]


def task_3(original_array, number_elements):
    """
    pick random num of elements from given array
    """
    if number_elements > len(original_array):
        return False
    fin_array = []
    for _ in range(number_elements):
        choice = randint(0, len(original_array) - 1)
        fin_array.append(original_array[choice])
        original_array.pop(choice)
    return fin_array

def task_4(original_array):
    """
    check if first and last element of array are equal
    """
    if len(original_array) <= 1:
        return False
    return original_array[0] == original_array[-1]

def task_5(array):
    """
    compute sum of elements in array
    """
    sum = 0
    for element in array:
        sum += element
    return sum

def task_6(original_array):
    """
    remove duplicates from given array
    """
    fin_array = []
    for element in original_array:
        if element not in fin_array:
            fin_array.append(element)
    return fin_array

def task_7(array_1, array_2):
    """
    check if two arrays have same first and last elements
    """
    return array_1[0] == array_2[0] and array_1[-1] == array_2[-1]

def task_8(original_array):
    """
    remove blank elements from given array
    """
    fin_array = []
    for element in original_array:
        if element != '':
            fin_array.append(element)
    return fin_array

def task_9(delimited_string):
    """
    split delimited string into array
    """
    return delimited_string.split(',')

def task_10(original_array):
    """
    create array with elements rotated left  of given array of ints length 3
    """
    return original_array[1:] + original_array[:1]


def task_11(original_array):
    """reverse array of ints length 3"""
    return original_array[::-1]

def task_12(original_array):
    """
    find largest element of array of length 3 and return array with all elements set to the largest element
    """
    max_element = max(original_array)
    return [max_element for _ in range(len(original_array))]

def task_13(array_arrays):
    """
    take array of arrays into 1 array
    """
    fin_array = []
    for array in array_arrays:
        fin_array.extend(array)
    return fin_array

def task_14(array):
    """
    check if given array contains 3 or 5 twice
    """
    return array.count(3) == 2 or array.count(5) == 2

def task_15(array):
    """
    find largest odd value in given array
    """
    array.sort()
    for element in array[::-1]:
        if element % 2 != 0:
            return element
    return None
