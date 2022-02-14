#Question 1

a=str(input("Enter any string: \n"))
list=a.split()
dict={} #an empty dictionary
if list.__len__()==1:   #check for single character or word
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   #else statement will be implemented when more than one word is entered in a string
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)


########################################

#Question 2

def Next_Date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):                
        day=int(input("Enter the day: \n"))
        if(1<=day<=31):
            break
        else:
            print("Please Enter a valid day")
    while(True):                 
        month=int(input("Enter the month: \n"))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    while(True):               
        year=int(input("Enter the year: \n"))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("Invalid date \n")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print(day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("Invalid date \n") 
            Next_Date()
            
    elif month in list3:
        if(year % 4 == 0):  
            if(day==29):
                day=1
                month=month+1
                print(day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("Invalid date \n")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("Invalid date \n")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1;
            print(day,"/",month,"/",year)
        else:
            print("Invalid date \n")
            Next_Date()
        
    else:
        print("Invalid date try again \n")
        Next_Date()
Next_Date()

#############################################

#Question 3

inplist = input('Enter elements of a list: \n')
user_list = inplist.split()
# print list
print('list: ', inplist)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(squarelist)

#################################################

#Question 4

def input_point():
    point = int(input("Enter Grade Point: \n"))
    if point>10 or point<4:
        print("Invalid grade point! \n")
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance \n")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance \n")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance \n")
elif(grade==7):
    print("Your Grade is 'B' and Good performance \n")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance \n")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance \n")
else:
    print("Your Grade is 'A+' and outstanding performance \n")

#################################################

#Question 5

x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()

##################################################

#Question 6

SID = int(input("Enter SID: \n"))
Name = input("Enter Name: \n")
students = {SID:Name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        SID = int(input("Enter SID: \n"))
        Name = input("Enter Name: \n")
        students[SID] = Name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("<a>",students)

#part b. sort acc to the names
print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c>",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("<d>",students[sid])

################################################

#Question 7

#  Function to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("Enter the number of terms in series: \n"))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer \n")
else:
   print("Fibonacci sequence: \n")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("Average of resultant fibonacci series is: \n",avg)

###################################################

#Question 8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)





