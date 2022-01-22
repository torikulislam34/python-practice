# take positive int input from user until negative value

'''a = []

while (True):
    i = int(input("Enter a int : "))
    if i < 0 :
        break
    else:
        a.append(i)
print (a)'''

from xml.etree import ElementInclude
 
#from pymysql import NULL
 
 
x = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
# take another int input from user. Slice the list as per 2nd input
s = int (input("Take slicer int"))
# pop inside for loop of s
index = 0
lenght_x = len(x)
while(index < lenght_x):
    mini_list = []
    counter = 0
    while(counter <s):
        if (len(x)>0): #if (x is not NULL): #
            mini_list.append(x.pop(0))
        counter += 1
        index +=1
    print(mini_list)

    x = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
for element in x:
    y = x.pop(0)
    print('Result of one pop(0): ', ' y=', y, ' x=', x)
print(' -------------------------------- ')
x = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
for element in x:
    y = x.pop()
    print('Result of one pop(): ', ' y=', y, ' x=', x)
 
 
 
"""
x = [100]
y = 0
print('before pop: ', 'list: ', x, 'y: ', y)
print(' ------------ ')
y = x.pop(0)
print ('after pop: ', 'list: ', x, 'y: ',  y)
print(' ------ Error ------ ')
y = x.pop(0)
"""
 
x = [1,2,3,4,1,5,1,2,10,5]
result = {}
 
for value in x:
    if value not in result:
        result[value] = 1
    elif value in x:
        result[value] += 1
print(result)
 
 
from collections import Counter
print(Counter(x))
 

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        if (self.b != 0):
            return self.a / self.b
        else:
            return "Cannot divide by zero."
 
 
    def do_square(self):
        self.a = self.a * self.a
        self.b = self.b * self.b
   
    def get_current_value(self):
        return self.a
        return self.b
       
Calc = Calculator(4, 3)
 
result = Calc.add()
print(result)
 
result = Calc.sub()
print(result)
 
result = Calc.mult()
print(result)
 
result = Calc.div()
print(result)
 
Calc.get_square()
print(' --- ', Calc.add(), Calc.sub())
Calc_2 = Calculator()
print('Another Calculator',Calc_2.addition())