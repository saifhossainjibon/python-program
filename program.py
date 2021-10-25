# even odd 
takeNumber =int(input("give number for check even/odd: "))
if takeNumber %2 ==0:
  print("number is even")
else:
  print("number is odd")

#  program 1
print("saif \n 018")
print("saif \t 018")
print("\"saif\"")
print("\'saif\'")
#  program 2
name ="Saif Hossain Jibon"
Age= 23
print("I'm "+name+"."+" I am",Age,"year old.")

# basic numercial operation
a=18
b=4
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(4**2)
print(a//b)
#  program 3
# getting user input
# name=input("name: ")
# age=input("Age: ")
# cgpa=input("Cgpa: ")
#
# print("My information")
# print("---------------")
# print("---------------")
# print("name: "+name)
# print("age:",age)
# print("cgpa:",cgpa)

num1=float(input("num1: "))
num2=float(input("num2: "))

area =0.5*num1*num2
print(area)
#  program 4
from math import *
print(max(20,10))
print(min(20,10))
print(abs(-20))
print(pow(2,3))
print(sqrt(25))
print(round(25.54))
print(floor(5.7))
print(ceil(5.7))
#  program 5
# num1=20
# num2=10
# print(type(num1))

num1=20
num2=10
print(f"{num1}+{num2}={num1+num2}")

print("saif hossain jibon")
print("01886431831")
# if you want to print in a single line
print("saif hossain jibon",end=" ")
print("01886431831")
#  program 6
print(20>10)
print(20<10)
print(20>=10)
print(20<=10)
print(20==20)
print(20!=10)
#  program 7
num1=80
num2=60
num3=90

if num1 >num2:
  if num1> num3:
    print(num1)
  else:
      print(num3)

if num2 >num1:
  if num2> num3:
    print(num2)
  else:
      print(num2)
#  program 8
ch = 'a'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
  print("vowel")
else:
  print("consonant")
#  program 9
a =int(input("Give a number: "))
b =int(input("Give a number: "))
c =int(input("Give a number: "))
d =int(input("Give a number: "))

if(a>b and a>c and a>d):
  print("A is big")
elif (b>c and b>d):
  print("B id big")
elif (c>d):
  print("C is big")
else :
  print("D is big")
# program 10
# i =1
# while i<=100:
#     print((i))
#     i = i+1
# print("End")

i =2
while i<=20:
    print(i)
    i = i+2
print("End")

i =1
while i<=20:
    print(i)
    i = i+2
print("End")