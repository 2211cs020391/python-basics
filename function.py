# -*- coding: utf-8 -*-
"""function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jQJVKt_Qga4BJBzOQA4C0pbYSlpP5u69
"""

def greet(name):
  print("hello "+name)

greet("sanjay")

name = "Rahul"
print(name.upper())
print(name.lower())
print(name.swapcase())

first_name = "Rahul"
last_name = "Dravid"
full_name = first_name + " " + last_name
print(full_name)

text = "Hello, world!"
substring = text[0:5]
print(substring)

text = "Hello"
length = len(text)
print(length)

text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)

text = "Hello, world!"
position = text.find("d")
print(position)

a ="1234asa"
b=a.isdigit()
print(b)



a=range(20)
print(a)
b= list(a)
print(b)



def add_numbers(a,b):
  result=a+b
  return result
add_numbers(2,3)



def greet(name):
  print(f"Hello, {name}!")

greet("Sanjay")



def calculate_sum(*args):
  total= sum(args)
  return total
result=calculate_sum(1,2,3,4,5)
print(result)



correct_username = "admin"
correct_password = "password123"

while True:
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  if username == correct_username and password == correct_password:
    print("Login successful!")
    break
  else:
    print("Incorrect credentials")



def factorial(number):
  result = 1
  while number > 1:
    result *= number
    number -= 1
  return result

num = int(input("Enter a non-negative integer: "))

fact = factorial(num)
print("The factorial of", num, "is", fact)



my_list = [1, 2, 3]
print(dir(my_list))



def even_numbers(n):
  total = 0
  for i in range(2, n + 1, 2):
    total += i
  return total

n = int(input("Enter a positive integer: "))

sum_even = even_numbers(n)
print("The sum of even numbers from 1 to", n, "is", sum_even)