# Fundamental DataType
#Math Functions
# round()
# abs( This function is for absoulte value only posity)
int
float

bool
#in booling 1=True and 0=False

str
#long_string ''' type here your comment '''
# to concatinate use +
#weather = "this is \"bullshit\""
#print(weather) This is how to do some cotation
# \t this is how have a tab at the beggining of the word
####Example of all with string#######
name = str(input('Please enter your name: '))
age = int(input('Please enter your age: '))
location = str(input('Please give us your location: '))
profesion = str(input('Please tell us your profession: '))
status = str(input('Please what is your status: '))
show = (f'\n\n \tMy name is {name}. \nI am {age} years old, \nand my location is {location} \nmy profession is {profesion} \nand I am \"{status}\"!')
print(show)

################This is the list portion############
list =[''] #can be modified and changed and replaced and it is odered and duplicate
#Matrix
x #This will print 5

#This is how to go through a matrix or list inside a list
picture = [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,0,1,0,0]
 ]
file = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel:
            print(file, end='')
        else:
            print(empty, end='')
    print(' ') #This for the new line of every row

#list slicing
my_list = [ 'apple','mango', 'bananna', 'orange', 'apple', 'bananna', 'kiwi', 'apple', 'starburry']
print(my_list.index('bananna'))
checker = 'mango' in my_list
print(checker)
my_list.append('peanaple')
my_list.remove('orange')
my_list.insert(3, 'carote')
print(my_list.count('apple'))
my_list[0] = 'fruits'

#This code here is how to cotrol a duplicate inside a list
duplicate = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print(f'This is the duplicated one in our list: {duplicate}')

#Methods
my_list = [ 'apple','mango', 'bananna', 'orange', 'apple', 'bananna', 'kiwi', 'apple', 'starburry']
#adding function
my_list.append('peanaple')
my_list.insert(3, 'graps')
my_list.extend(['jingar', 'leamonad'])
my_list.count('apple')
my_list.index('kiwi') #This will count how many kiwi are there
my_list.sort()
new_list = my_list.copy()
my_list.reverse()
my_list.pop()
# *******************This is not for list*************
# push, add
#############to join the list#############
new_list = ' '.join(['jingar', 'tamarin'])
print(new_list)

#Unpacking a list
a,b,c,d = [1,3,4,5]
print(a)
print(b)
print(c)
print(d)

#Unpacking a matrix
list = [
    [2,3,4],
    [3,2,1],
    [3,2,4],
    [3,2,6]
]
for row in list:
    for i in row:
        print(i, end=' ')
    print(' ')

#removing
my_list.pop(0)
my_list.remove('kiwi')
my_list.clear()
print(my_list)

#######################This is a tuple ################
#A tuple can not be assigned, added or modify
tuple = (1,3,4,5,6,6)
#This can be duplicate
tuple.count()
tuple.index(0)

###############This is the portion of set############
#All the element of a set has to be unique and no index like set[0]
sets = {1,3,5,6,7}
sets.add(22)
# this is to converte a list in a set by set(list_name)
#Method:
#.update('7') this like addeding something in the set but not float or int
#.difference() find the difference between two sets
#.discard(value) delete this value
#.intersection(), .union(), issubset(), .issuperset()

##############This is the dictionary part##############
#This is an unodereded. can hold any type of date. Keys has to be unique. and Unmutable
dict = {
    'one':181,
    'two':89,
    'age':'hello'
}
#Method:
dict.get('one') #This is how to access the element of the dictionary
'one' in dict.keys() #This is how to check if a key exists
181 in dict.values() #This is how to check if a values exists
dict.items() #This is how to get all items in the dictionary
dict.clear() #This is will clear the dictionary
dict.copy() #This will copy the dictionary
dict.pop('the name of the key') #this delete this key to the dictionary
dict.update({'age': 27}) #This how to update a dictionary

#Example############
user = {
    'name':'Mamadou',
    'is_student': True,
    'age': 27,
    'height': 6
}

#This is for the value
for i in user.values():
    print(i)

#This is the for the values
for i in user.keys():
    print(i)


#This is for all
for key, value in user.items():
    print(key, value)


#############This is how to make a username and password###############
username = str(input('Please enter your username: '))
password = (input('Please enter your password: '))
cha = len(password)
password_hiden = '*' * cha
print(f'Hi {username}, your password is {password_hiden}, and the length of it is: {cha} letters long')


#Ternary Operartor and short circuty:
is_eboard = False
is_alumni = True
if is_eboard and is_alumni:
    print('Go in')
else:
    print('Get Out')
is_me = False
is_yo = True

if is_me and is_me:
    print('You are a master magician')
elif is_me and not is_yo:
    print('you are getting tere')
elif not is_me:
    print('You need magic power')

# == cheks the values and is checks the location

#This is the way fo using enumerate
for i, num in enumerate('hello'):
    if num == 'l':
        print(f'The index of l is :{i}')

for i, num1 in enumerate(range(10)):
    print(i, num1)

#Function with default values
def one(name= 'Mamadou', age=24, level='student'):
    print(f'Hello there I am {name}, I am {age}. My level is {level}')

one('Boussouriou', 27, 'Junior student')
one()

#Functions have to return something always
def sum(num1, num2):
    return num1 + num2
print(sum(2, 4))

# *args and **kwargs
def supeer_func(*args,**kwargs):
    '''
     *args means we can have multiple arguments and retuens a tuple
     **kwargs means that we can have multiple arguments and returns a dictionary
    :param args:
    :return:
    '''

    return args, kwargs
print(supeer_func( 1,2,3, num1=3, num2=0))

#This is how to get the higest number in a list
def higest_even(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)

print(higest_even([20,10,2,3,7,11,40]))

# This is the goldman sach code on test
def fizzBuzz(n):
    # Write your code here
    count = 0
    while count <= n:
        count += 1
        if count == 3:
            print('Fizz')
            continue
        elif count == 5:
            print('Buzz')
            continue
        elif count == 6:
            print('Fizz')
            continue
        elif count == 9:
            print('Fizz')
            continue
        elif count == 10:
            print('Buzz')
            continue
        elif count == 12:
            print('Fizz')
            continue
        elif count == 15:
            print('FizzBuzz')
            break
        print(count)




#TODAY
#&&&&&&&&&&&&&&&&&&&&&&&&&7This is the OOP pillars 4 of them abstract, inheritance, polymorphisme

# This Exercise here is to find the oldest cat
class Cat:
    species = 'mammal'
    def __init__(self, name,age):
        self.name= name
        self.age = age
#Instantiate
cat1 = Cat('redose',3)
cat2 = Cat('ridose',5)
cat3 = Cat('rose',6)
#This is the function that finds the oldest one with many arguments
def get_oldest(*args):
    return max(args)
print(f'The Oldest cat is {get_oldest(cat1.age, cat2.age, cat3.age)}, years old!')


# This is the way to keep our methods private and public
class PrivateAndPublic():
    def __init__(self, name, age):
        self._name = name
        self._age = age
     #That means any uder score infront of a variable is a private please do not modify it Thanks
    def speak(self):
        return (f'This is {self._name}, the one that is making a lot of noisy here all the the time')
person  = PrivateAndPublic('Mamadou', 23)
print(person.speak())

# This is inheritance
# The subclasses can inherite the same parent class but they methods can be unique
#The super is used here

# This is the parent calss
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return ('Hey Dude you loged in')

# The parent class has to be passed in all the subclasses that are inheriting from it
#This is a subclass
class TypeOfGame1(User):
    def __init__(self, name, power,email):
        super().__init__(email)
        self._name = name
        self._power = power

    def attack(self):
        return (f'This player is attacking with a Power of {self._power}')

#This is a subclass
class TypeOfGame2(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self._name = name
        self._arrows = arrows

    def attack(self):
        return (f'This player has been using {self._arrows}  arrows')

# This is the instantiation here
game1 = TypeOfGame1('Mamadou', 30)
print(game1.attack())

game2 = TypeOfGame2('Diallo', 100)
print(game2.attack())


# This is the multi inheritance
# MRO method resolution order
# This is also a multilple inheratance case

class A:
    num = 10

class B:
    pass

class C(A):
    num = 5

class D(B, C): #The first argument has the pariority over the second
    pass

print(D.num)
print(D.__mro__)  #This is going to give us the work flow or the order of it
# Here is the logic as D has (C, B) Is going to check if D has something then C then B or their parents






#TODAY
############This is the section of the functional programming###########
#There are some sections for this portion too

# 1- pure functions
def multiply(li):
    new_list = []
    for i in li:
        new_list.append(i*2)
    return new_list

print(multiply([2,3,5]))
# The take away here is to make each number in the list by 2. this is a clean code

#2-maps
my_list = [1,2,4]
def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, my_list))) # This map is to affect all ements at the time
#That can be a SET, TUPLE,LIST but NOT a DDICT
#This Map section also does not affect the the list above
print(my_list)


#-3 Filter
my_list = [1,2,4,3,7]
def only_odd(item):
    return item % 2 != 0
print(list(filter(only_odd, my_list))) # This is how to filter something in a list
# That also can be a SET TUPLE OR LIST ONLY


#-3 Zipe
my_list = [1,2,4,3,7]
my_list1 = [4,5,7,9,0] # like () and []
# This can be a combine of many tuples and lists

print(list(zip(my_list, my_list1)))
# This is going to take the first elements together in a tuple and the second elements etec..


#-4 Reduce
from functools import reduce

my_list = [2,3,4,6]

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list, 0)) # The 0 is the default one cam be removed
# This REDUCE is to accumulate all the element in the list and give the total


###############this is the exercise of all 4 cases combine################
from functools import reduce

#1 Capitalize all the pets name and printthe list
#This is the map exercise
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(item):

    return item.capitalize() # This will capitalize the first letter of each element
    return item.upper() #This will capitalize the name of all the pets

print(list(map(capitalize, my_pets)))


#2 Zipe the 2 list into a list of tuple then sort numbers from lower to higer
my_strings = ['a', 'b', 'c', 'd','e']
my_numbers = [9,5,2,8,1]

resul = (list(zip(my_strings, sorted(my_numbers))))
print(resul)


#3 Fiter the list higer than 50 this is the exercise
scores = [73, 20, 65, 19, 88, 100, 76]
def hiher(item):
   return item > 50

print(list(filter(hiher, scores)))


#4 This is the reduce one to comibe all the numbers in the scores
scores = [73, 20, 65, 19, 88, 100, 76]
def accumulator(acc, item):
    return acc + item
print(reduce(accumulator, scores))


################## This is the lambda Expressions DOES NOT WORK ON ZIP###########
#Lambda with Map
my_list = [1,4,9]
print(list(map(lambda item : item * 2, my_list))) #this will mutiply each item by 2
# This id the LAMBDA expression using the map less code

#Lambda with filter
print(list(filter(lambda item : item % 2 != 0, my_list)))
# This id the LAMBDA expression using the filter less code

#Lambda with reduce
from functools import reduce
print(reduce(lambda acc,item :item+acc, my_list))
# This id the LAMBDA expression using the reduce less code

##############This is the exircise of lambda ############
#square with lambda
my_list = [3,5,9]
print(list(map(lambda item : item * item, my_list)))

#list sorting with lambda by the second number of tuples in the list
a = [(1,5),(0,3),(-1,2),(2,7)]

print(sorted(a))

a.sort()
print(a)
# These 3 lines of code above do the same sorting by the order first number

a.sort(key=lambda x: x[1])
print(a)
# This line of code here sorting the list by the second number


###########This is a list and set comprehension ##############
########fir set we just change the [] to () everything is the same########
# list of strings
my_list = [char for char in 'hello'] #This code here will append(hello) char by char
print(my_list)

# list of numbers
my_list2 = [num for num in range(0,100)] #This will print from 0 to 100
print(my_list2)

my_list3 = [num*2 for num in range(0,100)] #This here will multiply each num by 2
print(my_list3)

my_list4 = [num for num in range(0,50) if num % 2 == 0] # this one takes only even numbers
print(my_list4)


########This is dictionary comprehension###############
# This is the first example of dictionary comprehension
simple_dic = {
    'a': 1,
    'b': 2
}
my_dict = {k: v**2 for k, v in simple_dic.items() if v % 2 == 0}
print(my_dict)
#This code above here is going to create another dict and takes only the even values

#This is the second example where a list is given and that list is modify as a dict
my_dict2 = {num: num*2 for num in [1,2,3]} #The 1,2,3 is the key and their double is the value
print(my_dict2)


#################This is the compresion exercise###################
# this exercise is to get ride of all the duplicaated one in list be smart
some_list = ['a', 'b', 't', 'p', 'n', 'b', 'n']

duplicate = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicate)



#TODAY
###############This is the Decorators section###################
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func
# This functions above is the structure of the decorator


#This function down here is the use of the decorator anythin in the main the hell func has access
@my_decorator
def hell(name, age, height):
    print(name, age, height)

hell('Mamadou', 27, 5)


# This decorator function helps us find the performence of our function
from time import time

def performence(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'The time used is {t2 - t1} s')
        return result
    return wrapper

#This decorator tells us the time it takes for the function below to run
@performence
def log_run():
    for i in range(1000):
        return i * 5
log_run()


############This is the decorator exercise###########
#This function checks authentification for a user in a dictonary
user1 = {
    'name': 'Sorna',
    'valid': True
}
print(user1)
def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            result = fn(*args, **kwargs)
            return result
    return wrapper

@authenticated
def message_friends(user1):
    print(f'Hey {user1.get("name")} you are authenticated ') #This is how to get an element in a dictionary
    print('message has been sent')

message_friends(user1)


#############This section here is how to handle an error################
while True:
    try:
        age = int(input('Please enter your birth year: '))
        yr_age = (2020 - age)
        print(yr_age)

        div_age = 10/age
        print(div_age)

    except ValueError:
        print('Please enter a number') #This here is handling for int

    except ZeroDivisionError:
        print('Please enter a number hihger than ZERO!')# This is handling for 0 division

    else: #This else is to get out the loop when is true
        print('Thank you!')
        break

##########Another example #######
def sum(s1, s2):
    # This is how too handle many type of errrors at the same time
        try:
            return s1 / s2
        except (TypeError, ZeroDivisionError, ValueError) as err:
            print(err)
print(sum(1,0))



##############This is the generators section################
#YIELD and NEXT is the KEY here

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 10)
for i in gen:
    print(i)

####This is the fib number exercixe###
#This exercixe is ADDINF THE PREVIOUS NUMBER
# Here is the output
# 0
# 1
# 1
# 2
# 3 5 8 etc it does like the sum of the last 2 numbers  == to the next EXP: 3+5 =8
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(10):
    print(x)




#TODAY
#################This is the MODULE sections############
#Python built-in Moduls you can import them you can find all type in there

#This is a game gussing with random
from random import randint

answer = randint(1, 10)
while True:
    try:
        guess = int(input('Please guess a number from 1 to 10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('Bingo!')
                break
        else:
            print('Hey the number should be from 1 to 10!')

    except ValueError:
        print('Please enter a number')
        continue

#This is how to make jokes when you install pyjokes
import pyjokes
jok = pyjokes.get_joke('en', 'neutral')
print(jok)


#######This  the collections packages Counter defaultdict and OrderDict#####
from collections import Counter, defaultdict, OrderedDict

# 1-Counter
my_list = Counter([1,2,3,4,4])
#This Counter will tells us how many times each element exist and return in a dict
print(my_list)

# 2-defaultdict
my_dict = defaultdict(lambda: 5,  {'a': 1, 'b': 2})
#This defaultdict will assign any element that does not exist in the dict to 5
print(my_dict['h'])

# 3-OrderDict
d = OrderedDict()
d = 1
d = 2

d2 = OrderedDict()
d2 = 2
d2 =1

#This OrderDict wil check the Order of both dict even the numbers are the same if the order is not it will return false
print(d == d2)


############This is the Debuging Section########
import pdb #This one here is very useful to debud your code

def add(num1, num2):
    pdb.set_trace() #This is the line of code that you need to track the error but once you done with it you remove this line
    return num1 + num2


add(4, 8)


#########This is the file I/O section##############
# 1- Read a file mode= r and write mode= w  and appened mode= a and mode= r+ that means you can read and write
#This is how to read a file  You do not need to close it this way
with open('fileName', mode='r') as my_file:
    my_file.readlines()

# 3-  Write and Appened mode  w and a
#This is how to read a file  You do not need to close it this way
try:
    with open('fileName', mode='w') as my_file:
        my_file.write()
except FileNotFoundError as err:
    print('File not Found')
    raise err

except IOError as err:
    raise err

#This is how to acces files like file path That works for all of them
with open('folder/fileName', mode='w') as my_file:
    my_file.write()

######This section here is how to translate a file to any langauge####
from translate import Translator

translator = Translator(to_lang='ja')  # This JA stands for japanise any langage can be used

try:
    with open('text.txt', mode='r') as my_file:
        #This code here makes the translation
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)

        # Here we creating another file for the translate file
    with open('newFile', mode='w') as my_file2:
        my_file2.write(translation)
        # This 2 lines of code create a file for the translate

except FileNotFoundError as err:
    print('File Not Found')

#######################This section here for regular Expression###########
#This is how to check or set for a password the limit type of caracters
import re

#More search for on thi site re
patern = re.compile(r"[A-Za-z0-9@$%&]{8,}\d")

#Here is the condition [A-Zaz] That means all type of letters lower or Uper
#Here is the condition [0-9] That means numbers from 0 to 9 must to be in
#Here is the condition [&^%$#@!*] That means One of these must to be in
#Here is the condition for the limit {8,} That means at least 8 caracters
#Here is the condition that ends by a number \d OR [0-9] That means it ends by a number

#But in order to use it all together this way r"[A-Za-z0-9!@#$%^&*]{8,}\d"
re.compile(r"[A-Za-z0-9*&^%$#@!]{8,}\d")

password = 'Maa546e$3' #This is the password

checker = patern.fullmatch(password)

print(checker)



##TODAY######
#####################The Testing Section###########
#This is how we test our codes and functions
import unittest
import main #This main is the file that has the functions or the code

class TestMain(unittest.TestCase):
    def test(self):
        num = 10 #This is the value of num
        result = main.number(num) # This is from the main file with the function that we are testing
        self.assertEqual(result, 15) #The 15 is the expected result for true

    def test2(self):
        num = 0 # This is the num value
        result = main.number(num)
        self.assertEqual(result, 'please enter a n ber higher than 0')

    def test3(self):
        num = 'Kakaka'
        result = main.number(num)
        self.assertEqual(result, ValueError)

    def test1(self):
        num = '' #This is the value of num
        result = main.number(num)
        self.assertEqual(result, 'Please enter a number')

if __name__ == '__main__': # This line of code states that code under runs only when the main file is run
    unittest.main()   # This line of code is to run the the test





#TODAY
#####################This is the section of Scripting############
#########This is How to process images###########
from PIL import Image, ImageFilter

img = Image.open('photos/b.JPG')
filtered_image = img.filter(ImageFilter.BLUR) #This BLUR can be SMOOTH OR SHARPEN but support only png
filtered_image.save("blur.png", 'png') #This is going to create another image.

#######This is how to convert images too#########
from PIL import Image, ImageFilter

img = Image.open('photos/b.JPG')
filter_image = img.convert('L') #This L means that the photo will be gray
filter_image.save('grey.png', 'png') #create the grey image can be any name
filter_image.show() # This is going show the image

###############This is how to rotate an image###########
from PIL import Image, ImageFilter

img = Image.open("photos/b.JPG")
filter_image.convert('L')#This is not needed here is optional
rottate = filter_image.rotate(90)#This is going to rotate th image 90
rottate.save("grey.png", 'png') #This is going to save it can be any name
rottate.show()#This is going to show it like print


########This is how to resize an image########
from PIL import Image, ImageFilter

img = Image.open("photos/b.JPG")
filter_image.convert('L') #This is not needed here if you want
resizze = filter_image.resize((200, 200))#This is going to resize and has to be tuple ()
resizze.save("grey.png", 'png')# can be any name
resizze.show()

##########This is how to make a profile image#########
from PIL import Image, ImageFilter

img = Image.open("photos/b.JPG")
# Here we do not need to give any variable as above becaus ewe just modify we are not make another image
img.thumbnail((400, 400)) # The 400 is the max thumbnail will make the rest like great and the THUMBNAIL is the use one
img.save('anyname.png')
img.show()

##############This is the exercise for images####### PNG is the use one
#here is how to make all the images look the same no matter what
import os
import sys
from PIL import Image

image_folder = './photos'

for image in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{image}')
    img.thumbnail((400, 400)) #This line here is going to make all the images at the same format
    clean_name = os.path.splitext(image)[0] #This line here is going to make the name .png
    img.save(f'{image_folder}/{clean_name}.png', 'png')
    img.show()


###########This is how to deal with pdfs##########
#To use pdf install PyPDF2. pip3 install PyPDF2
import PyPDF2

with open('uber.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(page)
#The writting is the same too you just need to change read to write

##########This is how to combine pdfs##############
import PyPDF2
import sys

inputs = sys.argv[1:] #That means all he filles in the directory

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() #This is the one that is going to make all the filles together
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')#This line here will create the new file with all the pdfs

pdf_combiner(inputs)


####This is how to add a watermark in all pages#######
import PyPDF2

template = PyPDF2.PdfFileReader(open('name of the file has all the pages.pdf', 'rb'))# This line has all the pdfs
watermark = PyPDF2.PdfFileReader(open('name of the watermark.pdf', 'rb'))#This line is where the watermark is
output = PyPDF2.PdfFileWriter() #This is the line for the out put

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))#The page is one here that is the reason of 0
    output.addPage(page)
#This for loop does all the work for the combine of the watermark

with open('Name of the new file that you creating with the watermark .pdf', 'wb') as file:
    output.write(file)


###This is how deal with csv files the better way to store infos than pdfs###
import csv
name = input('please enter your name: ')
age = int(input('please enter your age: '))
#These two lines here can be a function that has the data comming from the user
def csv_file(date):#That is a function then we just need to call that function and passe the argument that has the data
    with open('database.csv', newline='', mode='a') as data:
        csv_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #This line above here is the one that is intanct except the DATA variable
        csv_writer.writerow([name, age])#This is the one that is going t write the file


#######This how to send email with python#########
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())# This is the path to the html file

email = EmailMessage()
email['from'] = 'Mamadou Diallo'
email['to'] = 'boussouriouy@gmail.com'
email['subject'] = 'you got me dude'

email.set_content(html.substitute({'name': 'Tata'}), 'html') #This is a variable from the html file

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('codding912@gmail.com', 'Baben251551') #This is email that send the emails like the company email
    smtp.send_message(email)
    print('All good dude')

#$$$$$$$$$$$$this is a site to check if your email or passwor have been hacked####
#haveibeenpwned.com

#############SMS SENDING###################
#This is how to send messages to someone  WE USE TWILIO an ACCOUNT has to be open for it
#First we have to install TWILIO by pip install twilio

from twilio.rest import Client

account_sid = 'AC3be8d8c2ddbc720f7edf0b01cac1bfe1'
auth_token = 'c11173ec2ff9081cdf84f3972309cc7a' #This token is just for my number
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12054311924', #This is the num that twilio give you
    body='Dude you going to be killing me',
    to='+13476795211'
)

print(message.sid)


##TODAY
#################This is the web scripting section#############
##The HACKERNEWS is a very good website to visit for a programmer to get uptadate
#In order to script a web in python we download BEAUTIFULSOUP4 and REQUESTS first
import requests
from bs4 import BeautifulSoup #this line allows us grap data from html

res = requests.get('https://news.ycombinator.com/news')#This the url where we want grab the data
soup = BeautifulSoup(res.text, 'html.parser')#This line here gets the text and convert it to an html
soup.title or soup.body #that gives us the title and body
soup.find_all('a') #This will allow us to get all the tags can be div or span or anytag

#The best way to grab things is this way

soup.select('classes, ids, or all tags')
soup.select('.nameOfTheClass or id')
links = soup.select('.storylink')# This is the a links
votes = soup.select('.score')#This is the value of the story
#Down here we have to do functions or loops that we want do display the data


#############This section is how to do automation/testing #########
#This is how to test/Automations
#WE have to install SELENIUM for that

from selenium import webdriver
variable = webdriver.chrome('./ we passe the the chrome driver here PATH')#To find drivers just go SELENIUM PYTHON DRIVER

variable.get('WE PASS THE URL WERE WE WANT TO GRAB THINGS ')

assert 'someting' in variable.page #The PAGE cen be REPLACED by TITLE or BODY
#This line above here is how to find something or search for something

var1 = variable.find_element_by_id('we pass the id here from the url')
var1.clear() # This will completly clear
var1.send_keys('Type message here') #This is going to write that message on the url

var2 = variable.find_element_by_class_name('passe the or the button')
var2.click() # this will automatically click the button for you

variable.close()
variable.quit()
# These two lines will close the browser or quit them

##############This is the machine learning section
# we use these libraries  NUMPY, PANDAS, SCIKIT-LEARN, and MATPLOTLIB and SEABORN, BOKEH



##TODAY
#####This section is about GIT and GETHUB
# we can change the MASTER like name it something else that we can make changes and someone on the team can see and aproev then merge it.
#here is th workflow
#git branch    #to check how many branches are there
#git branch nameOfBranch you want create    # This is a unique branch for you to work on then push it
#git checkout -b NameOfBranch      #This is the shortcut of creating this quikly
#git checkout nameOfBranch         # Then you good to make your changes and push it
#git diff         #This alos will show all the changes






