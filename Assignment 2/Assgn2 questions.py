Assignment 2

# Question 1
string1="Python is a case sensitive language" 
print("<A>THE LENGTH OF STRING IS",len(string1))
print("<B>THE REVERSED STRING IS ",string1[::-1])
string2=string1[10:26] #Stored a case sensitive in a new string
string2.replace("a case sensitive","object oriented") 
print("<E>THE INDEX OF SUBSTRING a is ",string1.find('a'))
print("<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))


#########################################################################

#Question 2
NAME=input("ENTER YOUR NAME \n")
SID=int(input("ENTER YOUR SID \n"))
DEPARTMENT=input("ENTER YOUR DEPARTMENT \n")
CGPA=float(input("ENTER YOUR CGPA \n"))
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPARTMENT,"and my CGPA is %f"%CGPA)

##########################################################################

#Question 3
a=56
b=10
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)

##########################################################################

#Question 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 >=num2) and (num1 >=num3):
   largest = num1
elif (num2 >=num1) and (num2 >=num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is: \n",largest)

##########################################################################


#Question 5
s=input("Enter a string: \n")
if 'name' in s:
    print ("Yes")
else:
    print ("No")

###########################################################################


#Question 6

a=float(input("Enter FIRST side of triangle: \n"))
b=float(input("Enter SECOND side of triangle: \n"))
c=float(input("Enter THIRD side of triangle: \n"))
if(a>=(b+c)):      #Equality sign is used because if sum of two sides is equal to third then also triangle is not valid
    print("No")
elif(b>=(a+c)):
    print("No")
elif(c>=(a+b)):
    print("No")
else:
    print("Yes")    
