"""
print('Spam Eggs')
print("Paris rabbit got your back :)! Yay!")
print('2002')


print('don\'t')
print("don't")
print('"Yes," They said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

jayvier = int(input("Enter first number: "))
BUNIjords = jayvier * 3
print(BUNIjords)
"""

#indexing
"""
var = "HElloworld"
print(var[0:5])
print(var[-1])

text = input("Input word: ")
index = int(input("Input number: "))
print(text[index])
print(len(text))
"""

#slicing
"""
xmple = "hello world"
print(xmple[-5:])  #world
print(xmple[-8:-6])  #lo
print(xmple[0:5], "i am aljieo tolibas")  #hello i am aljieo tolibas
print(xmple[0:5], xmple[-5:])  #hello world
print("{1} {0}".format(xmple[0:5], xmple[-5:-2]))  #wor hello
print(f"{xmple[0:2]} {xmple[6:8]}")  #he wo
"""

#string methods
"""
word = "HeLlO2woRlD"
print(word.upper())  #HELLO2WORLD
print(word.lower())  #hello2world
print(word.capitalize())  #Hello2world
print(word.title())  #Hello2World
print(word.replace("H", "x"))  #xeLlO2woRlD
print(word.isalpha())   #False
print(word.find("w"))  #6
print(word.isnumeric())  #False
print(word.isalnum())  #True
"""

word = "summer bootcamp"
print(word.title())
print(word.capitalize().replace("p", "P"))
print(word.replace("b", "l")[7:11])
print(word.replace("p", "E")[11:])
print(word[-3].upper() + word[5].upper())
print(word.replace(" ", "").isalpha())



