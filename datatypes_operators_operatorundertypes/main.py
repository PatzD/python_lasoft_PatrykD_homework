import sys
from datetime import datetime


def task_1():
    """
    program to get version of python
    """
    return sys.version


def task_2():
    """
    program to display current date and time
    """
    return datetime.now()


def task_3(copies, given_string):
    """
    program to create new strign which is n copies of given string
    """
    return copies * given_string


def task_4(radius):
    """
    compute area and perimiter of circle
    """
    area = 3.14 * radius**2
    perimiter = 2 * 3.14 * radius
    return area, perimiter


def task_5(string):
    """
    check if string starts with if
    """
    return string.startswith("if")


def task_6(first_name, last_name):
    """
    accept users first and last name and print them in reverse
    """
    return "hello" + last_name + " " + first_name


def task_8(num_1, num_2, num_3):
    """
    checks 3 numbers and returns true if one or more of them are small(1-10 and inclusive)
    """
    return num_1 in range(1, 11) or num_2 in range(1, 11) or num_3 in range(1, 11)


def task_9(num_1, num_2, num_3):
    """
    checks 3 numbers to see if one only is small
    """
    smalls = 0
    if num_1 in range(1, 11):
        smalls += 1
    if num_2 in range(1, 11):
        smalls += 1
    if num_3 in range(1, 11):
        smalls += 1

    if smalls > 1:
        return False
    else:
        return True


def task_10():
    """
    prints multiline here document
    """

    multi_line_string = """
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

    return multi_line_string

def task_11(og_string):
    """
    create string that starts with 'if', returns original if already beginning with 'if'
    """
    if og_string.strip().startswith("if"):
        return og_string
    return "if " + og_string

def task_12(og_string, copies):
    """
    creates new string using first 3 characters of original string or whatever is available, returns n copies of new string
    """
    return copies * og_string[:3]

def task_13(radius):
    """
    calculate volume of sphere
    """
    return 4/3 * 3.14 * radius**3

def task_14(og_string):
    """
    return new string where first and last letters are swapped
    """
    return og_string[-1] + og_string[1:-1] + og_string[0]

def task_15(int_1, int_2):
    """
    check if one int is 20, else add them and return that value
    """
    if int_1 == 20 or int_2 == 20:
        return True
    return int_1 + int_2

def task_16(num_1, num_2, num_3):
    """
    find greatest of 3 numbers
    """
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_1 and num_2 > num_3:
        return num_2
    else:
        return num_3

def task_17(num):
    """
    check if num is within 10 or 100 or 200
    """
    if num in range(10, 101):
        return True
    elif num in range(100, 201):
        return True
    else:
        return False

def task_18(num_1, num_2):
    """
    compute sum of two nums, if nums are equal return double the sum, otherwise return sum
    """
    if num_1 == num_2:
        return 2 * (num_1 + num_2)
    return num_1 + num_2

def task_19():
    """
    prints 'Python Basic Exercises' 9 times
    """
    for _ in range(9):
        print("Python Basic Exercises")

def task_20(og_string):
    """
    adds last character of string at beginning and end of string
    """
    if len(og_string) < 1:
        raise ValueError("string is empty")
    return og_string[-1] + og_string + og_string[0]

def task_21():
    """
    print 34 to 41
    """
    for i in range(34, 42):
        print(i)

def task_22():
    """
    prints even numbers between 1 and 10
    """
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)

def task_23():
    """
    print odd numbers from 10 to 1
    """
    for i in range(10, 0, -1):
        if i % 2 != 0:
            print(i)

def task_24(original_array):
    """
    prints elements of list
    """
    for element in original_array:
        print(element)

def task_25(num_1, num_2):
    """
    check two non negative integers and see if they have same last digit
    """
    if num_1 < 0 or num_2 < 0:
        raise ValueError("numbers must be non negative")
    return num_1 % 10 == num_2 % 10
