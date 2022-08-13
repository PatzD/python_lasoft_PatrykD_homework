#1. define class name Circle with two methods which compute area and perimeter of circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    def area(self):
        return self.pi * self.radius ** 2
    def perimeter(self):
        return 2 * self.pi * self.radius


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