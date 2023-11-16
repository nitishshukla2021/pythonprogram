#!/usr/bin/env python
# coding: utf-8

# In[1]:


#looping 
# here you have to be very careful of indentation


# In[ ]:





# In[7]:


i=1
while i<10:
    print(i)
    i=i+3


# In[8]:


i=1
n=6
while i<n:
    print(i)
    i=i+1


# In[9]:


# write a programe to calculate sum of 5 natural numbers


# In[11]:


n=int(input("enter total number:"))
i=1 
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print('addition of numbers:',sum)


# In[12]:


#important ques..=write a program to find a sum of 10 natural number?


# In[1]:


n=int(input("enter total number:"))

i=1 
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print('addition of numbers:',sum)


# In[2]:


# write a programe to find a sum of a natural number 


# In[1]:


n=int(input("enter the number:"))
i=1 
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print('addition of numbers:',sum


# In[2]:


# write a programe to check wheather the given number is positive,negative or zero


# In[4]:


b=int(input("enter the number"))
if b<0:
  print("entered number is negative")
elif b>0:
  print("entered number is positive")
else:
   print("entered number is zero")


# In[4]:


# wap to check wheather given number is positive,negative or zero.


# In[5]:


a=int(input("enter first given number a: "))
b=int(input("enter second given number b: "))
print("value of a is :",b)
print("value of b is:",a)


# In[6]:


# wap to swap two numbers using third variable.


# In[1]:


a=int(input("enter the number" ))
b=int(input("enter the number"))
temp=a
a=b
b=temp
print("a=",b)
print("b=",a)


# In[2]:


p=float(input("enter your principal amount:"))
t=float(input("enter your time:"))
r=float(input("enter your rate:"))
x=(p*t*r)/100
print("simple intrest is:",x)


# In[4]:


p=float(input("(1)enter your principal amount:   "))
t=float(input("( 2) enter your time:  "))
r=float(input("(3) enter your rate:   "))
x=(p*t*r)/100
print("(4) simple intrest is:    ",x)


# In[1]:


# while loop (break,continue) 
# break:- statement can stop the loop even the while condition is true
# continue:- statement can stop current hydration and continue with the next line
# forloop:- is used for over a (sequence) list, tuple,dictionary,string.


# In[3]:


i=1
while(i<6):
    print(i)
    if i==3:
        break
    i=i+1


# In[6]:


i=0
while(i<6):
    i=i+1
    if i==3:
        continue
    print(i)


# In[7]:


i=1
while(i<6):
    print(i)
    i=i+1
else:
    print("i is greater than 6")


# In[8]:


list1=[1,2,3,4,5]
for i in list1:
    print(i)


# In[9]:


list2=['a','b','c','d']
for i in list2:
    print(i)


# In[10]:





# In[1]:


# for loop: A is used to iterating over a sequence (that is either a list,a tuple,a dictionary,a set, )


# In[2]:


cars=["ford","audi","bmw"]
for i in cars:
    print(i)


# In[3]:


#break statement can stop the loop before it has loop prove for all the iteam


# In[5]:


cars=['ford','audi','maruti']
for i in cars:
    if(i=="audi"):
        break
    print(i)


# In[6]:


cars=['ford','audi','maruti']
for i in cars:
    print(i)
    if (i=="audi"):
        break


# In[7]:


cars=['ford','audi','maruti']
for i in cars:
    if(i=="audi"):
        continue
    print(i)


# In[8]:


# range funnction= range function returs a sequence of numbers starting from zero by default and increment by 1
#and end at a specified number


# In[9]:


for i in range (2,6):
    print(i)


# In[10]:


for i in range (2,30,3):
    print(i)


# In[13]:


for i in range(5,55,5):
    print(i)


# In[14]:


cars=['ford','audi','maruti']
for i in cars:
    print(i)
    if(i=="audi"):
        continue
    


# In[19]:


for x in range(6):
    if x==3:
        break
    print(x)  
else:
         print("finally finished")


# In[ ]:


# question= write a programe to find a sunm of sqare of an natural number


# In[4]:


n = int(input("Enter a natural number: "))
sum=0
if n<0:
    print("enter a positive natural number")
else:
    for i in range(1,n+1):
         sum=sum+(i**2)
    print("your sum is:",sum)


# In[6]:


n=int(input("enter a natural number:"))
sum=0
if n<0:
    print("enter a positive natural number")
else:
    for i in range(1,n+2):
        sum=sum+(i**3)
    print("your sum is:",sum)


# In[1]:


# function is a block of code which only runs when it is called we can pass data known as parameter into a function.
# function can return data as a result .
# modeul is also known as function.


# In[2]:


# creating function:- def my_fun():
print("hello aaft")


# In[3]:


#calling function:-fun()


# In[7]:


def my_fun():
    print("hello aaft")


# In[9]:


my_fun()


# In[10]:


# types of function:-1 built in function -standared function available in python
# user defined fuction:- we can creat our own function based on requirement


# In[11]:


# arguement are specified after function name inside the parenthessis.
# parameter is the variable listed inside the parenthessis in the function defination 
# an arguement is the value that is sent to function when it is called.


# In[12]:


# defining and calling a function with parameter.


# In[13]:


def addition(n1:int,n2:int):
    n3=n1+n2
    return n3
n1,n2=5,10
result=addition(n1,n2)
print("addition value is",result)
    


# In[21]:


def swap(x,y):
    return y,x
x=5
y=10
x,y=swap(x,y)
print("swap",x,y)


# In[19]:


# Q:wap to find wheather given number is prime or not?
# q: wap to find wheather given number is armstrong or not?
#q; wap to find given number is palindrome or not?


# In[1]:


#  types of function arguement:-
#1 default arguement
#2 keyword arguement(named arguement)
#3 positional arguement
#4 arbitrarry arguement(1 * arguement,2 ** arguement)


# In[5]:


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False


# In[2]:


#1 default arguement:-a default arguement is parameter that assumes a default values if a value is not provided in the function called.


# In[3]:


#2 key word :- its allows the caller to specifies the arguement name with value.


# In[4]:


#3 positional argurment:- it is called during the function called so that the first value assinged to some value and second value assinged to some other value.


# In[6]:


#4 arbitrary arguement:- *arguement means non key word arguement
# ** arguement :- keyword arguement


# In[9]:


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Input a number from the user
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# In[10]:


#  return statement:- return statement ends the execution of a function and returns control the calling function.
# a return statement can return a value to  the calling function


# In[5]:


# Input a number from the user
try:
    num = int(input("Enter a number: "))
    if  is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# In[4]:


a=int(input("enter the number:"))
if a<100000:
    print("enter number is gareb:")
elif a>100000:
    print("enter number is wealthy:")
else:
    print("enter number is rich:")


# In[1]:


#1 factorial:
#2 armstrong:
#3 reverese:
#4 prime no:
#5 palindrome:
#6 fibonacci series:


# In[6]:


n=int(input("enter the number "))
i=1
count=0
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("number is prime")
else:
    print("number  is not prime")


# In[8]:


# armstrong no:

i=int(input("enter number"))
x=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if(x==sum):
    print("number is armstrong")
else:
    print("number is not armstrong")


# In[ ]:




