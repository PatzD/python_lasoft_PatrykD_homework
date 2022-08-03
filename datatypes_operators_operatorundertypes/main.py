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
    return num_1 in range(1, 10) or num_2 in range(1, 10) or num_3 in range(1, 10)


def task_9(num_1, num_2, num_3):
    """
    checks 3 numbers to see if one only is small
    """
    smalls = 0
    if num_1 in range(1, 10):
        smalls += 1
    if num_2 in range(1, 10):
        smalls += 1
    if num_3 in range(1, 10):
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