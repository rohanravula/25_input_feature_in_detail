# a=input("Enter your name :") # if their is number we can conver into str, int,float.  but if in case we have letter we can only convert into str not in int or float if we try to convert we will be getting the error
# print("My name is",a) #My name is 25
# print("My name is",a,sep="-") #My name is-25
# print("My name is",int(a)) #My name is 25
# print("My name is",float(a)) #My name is 25.0
# print("My name is"+'       '+str(a)) #My name is         25 
# print("My name is"+" "+(a)) #My name is 25


# name=input("Enter your Name :")
# age=int(input("Enter your age :"))
# per=float(input("Enter your graduation percentage :"))
# print(name,age,per) #We can print any thing first age then name then per our wish

# name=input("Enter your name :")
# age=int(input("Enter your age:"))
# per=float(input("Enter your graduation percentage :"))
# #the below output will give in one line.
# print("your name is", name,"your age is",age,"and your graduation percentage is",per) #your name is rohan your age is 20 and your graduation percentage is 80.88

"to add this % symbole we need to conver the graduation percentage into str"
# name=input("Enter your name :")
# age=int(input("Enter your age:"))
# per=float(input("Enter your graduation percentage :"))

# print("your name is", name,"your age is", age, "and your graduation percentage is", str(per),"%") #your name is Rohan your age os 20 and your graduation percentage is 80.82 %
 
"different types to write in output"
# name=input("Enter your name :")
# age=int(input("Enter your age:"))
# per=float(input("Enter your graduation percentage :"))

# print("your name is{} your age is{} and\
# your graduation percentage is {}"format(name,age,per))

# print("your name is {2} age is {0} and graduation percentage is {1}".format(age,per,name)) #this is with index number

# print(f"your name is {name} your age is {age} and your graduation percentage is {per}%") #we can name the variable in flower bracket also.

"sum of two or multiple values"
# a,b=[float(x)for x in input("enter any two number : ").split()]
# print(a+b) # 4+9=13.0 we wrote float we got 13.0 if we write int we will get 13

# a=[int(n)for n in input().split(",")]
# print(sum(a)) #4,6,8,9,10=37

"mltiplication of two or more values"
import math 
# a=[float (n) for n in input().split(",")]
# print(math.prod(a))

"sum of first and last number"
x=input()
print(int(x[0])+int(x[-1]))

