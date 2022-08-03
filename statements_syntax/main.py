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