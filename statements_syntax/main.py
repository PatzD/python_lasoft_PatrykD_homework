from array import array
from itertools import count
from random import randint
from xml.dom.minidom import Element


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


def task_16(og_array):
    """
    create array using first three elements of a given array
    """
    array = []
    for i in range(3):
        array.append(og_array[i])
    return array

def task_17(og_array):
    """
    return amount of even numbers in given array
    """
    total = 0
    for element in og_array:
        if element % 2 == 0:
            total += 1

def task_18(og_array):
    """
    find diffrence between largest and smallest number in given array
    """
    maxim, minim = 0, 0
    for element in og_array:
        if element > maxim:
            maxim = element
        if element < minim:
            minim = element
    return maxim - minim

def task_19(og_array):
    """
    calculate average of elements in given array expect largest and smallest value
    """
    maxim, minim = max(og_array), min(og_array) 
    total = sum(og_array) - maxim - minim   
    return total / (len(og_array) - 2)
     
def task_20(og_array):
    """
    calculate sum of numbers of given array except the number 17 and numbers that come immediately after a 17
    """
    total = 0
    for element in og_array:
        if element == 17:
            break
        total += element
    return total

def task_21(og_array):
    """
    calculate sum of every 3rd element of array
    """
    total = 0
    for i in range(0, len(og_array)):
        if (i + 1) % 3 == 0:
            total += og_array[i]
    return total

def task_22(og_array):
    """
    check whether all elements in array are a 3 or a 5
    """
    return all(element % 3 == 0 or element % 5 == 0 for element in og_array)

def task_23(og_array):
    """
    check whether given value appears everywhere in array
    """
    return og_array.count(og_array[0]) == len(og_array)

def task_24(og_array):
    """
    check whether array contains a 3 next to a 3 or a 5 next to a 5 but not both
    """
    threes = False
    fives = False
    for i in range(len(og_array) - 1):
        if og_array[i] == 3 and og_array[i + 1] == 3:
            threes = True
        if og_array[i] == 5 and og_array[i + 1] == 5:
            fives = True
    if threes and fives:
        raise ValueError('Array contains both 3 and 5 next to each other')
    return threes or fives

def task_25(og_array):
    """
    check whether array contains two 6 next to each other or two or three 6 separated by one element
    """
    for index in range(len(og_array) - 1):
        sixes = 0
        if og_array[index] == 6 and og_array[index + 1] == 6:
            return True
        for i in range[0,4]:
            if i == 2 and sixes == 1:
                return True
            if og_array[index + i] == 6:
                sixes += 1
            if sixes == 2 or sixes == 3:
                return True
    return False

def task_26(og_array):
    """
    check if there is a 2 in the array and a 3 later somwhere
    """
    two = False
    three = False
    for element in og_array:
        if element == 2:
            two = True
        if element == 3 and not two:
            three = True
    return two and three

def task_27(og_array):
    """
    convert 2 dimensional array into dictionary
    """
    dictionary = dict()
    for i in range(len(og_array)):
        if og_array[i][0] not in dictionary:
            dictionary[og_array[i][0]] = []
        dictionary[og_array[i][0]].append(og_array[i][1])
    return dictionary

def task_28(og_array):
    """
    find most occuring item in array
    """
    dict = {}
    for element in og_array:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return max(dict, key=dict.get)
        
def task_29(og_array):
    """
    check if all elements in array are identical
    """
    temp = og_array[0]
    for element in og_array:
        if element != temp:
            return False
    return True

def task_30(start, og_array):
    """
    search items starting with certain letters in array
    """
    return [element for element in og_array if element.startswith(start)]

def task_31(og_array):
    """
    iterate array in reverse
    """
    return og_array[::-1]

def task_32(og_array, n):
    """
    iterate over the first n elements of array
    """
    if n > len(og_array):
        raise ValueError('n is greater than array length')
    return og_array[:n]

def task_33(og_array):
    """
    sort array of strings by length
    """
    return sorted(og_array, key=len)

def task_34(og_array):
    """
    remove all 0s from array, fill elements on right side of last 0 with values -1
    """
    if 0 not in og_array:
        return og_array
    temp = False
    for i in range(len(og_array))[::-1]:
        if og_array[i] == 0:
            temp = True
            og_array.pop(i)
        if not temp:
            og_array[i] = -1
    return og_array

def task_35(og_array):
    """
    reorganize array, put all negative values first, then positive, 0 counts as positive
    """
    negative = []
    positive = []
    for element in og_array:
        if element < 0:
            negative.append(element)
        else:
            positive.append(element)
    return negative + positive

def task_36(og_array, number):
    """
    count number of times number appears in array
    """
    return og_array.count(number)

def task_38(og_array):
    """
    array with size 10, show items that appear 2 or more times in array
    """
    return [element for element in og_array if og_array.count(element) > 1]

def task_39(og_array):
    """
    return smalles odd value in array
    """
    return min(element for element in og_array if element % 2 == 1)

def task_40(og_array, k, side=False):
    """
    shift array cyclically by k elements, if side is True, shift to left, otherwise to right
    """
    if side:
        return og_array[k:] + og_array[:k]
    return og_array[-k:] + og_array[:-k]



            
        
        


