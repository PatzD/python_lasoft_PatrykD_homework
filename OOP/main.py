#1. define class name Circle with two methods which compute area and perimeter of circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pi = 3.14
        return pi * self.radius ** 2
    def perimeter(self):
        pi = 3.14
        return 2 * pi * self.radius


#2. define class rectangle constructed by length and width and method to compute area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

#3. define class to reverse string word by word
class Reverse:
    def __init__(self, string):
        self.string = string
    def reverse(self):
        return self.string.split(' ')[::-1]

#4. class to compute power of number to given exponent
class Power:
    def __init__(self, n, x):
        self.number = n
        self.exponent = x
    def power(self):
        return self.number ** self.exponent

#5. class to check validity of open and closed parentheses, (), [], {} in given string, must close in correct order
class Parentheses:  
    def __init__(self, string):
        self.string = string
    def check_parentheses(self):
        open_parentheses = ['(', '[', '{']
        closed_parentheses = [')', ']', '}']
        stack = []
        for element in self.string:
            if element in open_parentheses:
                stack.append(element)
            elif element in closed_parentheses:
                if len(stack) == 0:
                    return False
                if element == ')' and stack[-1] == '(':
                    stack.pop()
                elif element == ']' and stack[-1] == '[':
                    stack.pop()
                elif element == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

#6. define class lunch, initialize with menu string and method menu_price, if "menu 1" print "price 12.00" if "menu 2" print "price 13.40", else print "Error in menu"
class Lunch:
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            return "price 12.00"
        elif self.menu == "menu 2":
            return "price 13.40"
        else:
            return "Error in menu"

"""
7. define Point3D class that inherits from object inside the Point3D class,
initialize with z,y,z coordinates, define __repr__() to return '(%d, %d, %d)' % (self.x, self.y, self.z)
"""
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return '(%d, %d, %d)' % (self.x, self.y, self.z)

#8. define class songs, init with lyricsis as list, define method to return each lyric as seperate line
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)