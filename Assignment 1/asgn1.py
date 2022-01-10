#Assignment 1

#Question 1

num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))
num3 = int(input("Enter third number: \n"))

avg= (num1+num2+num3)/3

print("The average of these three numbers is: \n",avg)

#######################################

#Question 2

Gross_Income = int(input("Enter your gross income(in Dollars): \n"))
No_of_Dependants = int(input("No. of total dependants: \n"))

#All values are in dollars
Standard_deduction = 10000
Dependant_deduction = 3000
Tax_Rate = 0.20

Taxable_Income = Gross_Income - Standard_deduction - Dependant_deduction*No_of_Dependants
Tax = Taxable_Income*Tax_Rate

if Tax<0:
    Tax = 0


print("Your income tax is: \n",Tax)

#######################################

#Question 3

SID = int(input("Enter SID: \n"))
Name = input("Enter your name: \n")
Gender = input("Enter your Gender(M,F,U for unknown): \n")
Stream = input("Enter your stream: \n")
CGPA = float(input("Enter your CGPA: \n"))

Student = [SID, Name, Gender, Stream, CGPA]

print(Student)

#####################################

#Question 4

m1 = int(input("Marks of first student: \n"))
m2 = int(input("Marks of second student: \n"))
m3 = int(input("Marks of third student: \n"))
m4 = int(input("Marks of fourth student: \n"))
m5 = int(input("Marks of fifth student: \n"))

Marks = [m1, m2, m3, m4, m5]
print(Marks)

Marks.sort()

print(Marks)

#####################################

#Question 5(a)

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color.pop(3)

print(color)



#Question 5(b)

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color)

color[3:5] = ['Purple']
print("After removing 4th and 5th element and replacing them with 'Purple': \n")
print(color)







