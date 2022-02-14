#problem 1- write a python program to count the number of occurences of each word or character in the string entered by the user (count the number of occurences of each character only if the single word is entered by the user)

string1=input("Give a string-\n")
list1=[]
list2=string1.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:          # for 1 word
    for i in string1:      # i created a list with the characters
        list1.append(i) 
    for j in list1:        # i created a condition where all unique keys
        if j in d:         #get value 1 and when a key repeats it increases 
            d[j]=d[j]+1    #value by 1
        else:
            d[j]=1
    print(d)        

else:
    for i in list2:        # for multiple words
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t) 
    print("Done!")



#-----------X--------------X-------------X-------------X----------------X-----------------
#problem 2- Write a python script to print next date of input date. It msut meet following conditions(use if-elif)
# C1: 1<=month<=12
# C2: 1<=day<=31
# C3: 1800<=year<=2025

month=int(input("enter month-\n"))


if(month in[1,3,5,7,8,10,12]):
    day=int(input("Give day-\n"))
    if(1<=day<=31):
        year=int(input("Give year-\n"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date-","1/1/",year+1)
            elif(day==31):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month in[4,6,9,11]):
    day=int(input("Give day-"))
    if(1<=day<=30):
        year=int(input("Give year-"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(day==30):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):
    year=int(input("Give year-"))
    if(1800<=year<=2025):
        day=int(input("Give day-"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date-",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date-",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")
print("Done!")    


#------------X---------------X--------------X------------------X-----------------X----------------
#Problem 3- Write a python program to create a lsit of tuples with the first element as the number and second element as the square of the number
# E.g. list=[3,9,10]
# output : [(3,9),(9,81),(10,100)]

alist=[1,2,3,4,5,6,7,8,9,10]
list_with_tuples=[]
for i in alist:
    list_with_tuples.append((i,i**2))
print(list_with_tuples)


#----------------X------------------X-----------------X----------------X---------------X----------------------
#Problem 4- Write a program to prompt the user for grade between 4 and 10. If the grade is out of range print error message. If the grade is between 4 and 10. Print the grade and the performance usign the following:
#   LETTER GRADE            PERFORMANCE         GRADE POINTS
#   A+                      outstanding         10
#   A                       excellent           9
#   B+                      very good           8
#   B                       good                7
#   C+                      average             6
#   C                       below average       5
#   D                       poor                4                

#create if else statements

Grade_points=int(input("Give a number between 4 and 10 including them-\n"))
if(Grade_points==4):
    print("Performance=Poor")
    print("Letter Grade=D")
elif(Grade_points==5):
    print("Performance=Below Average")
    print("Letter Grade=C")
elif(Grade_points==6):
    print("Performance=Average")
    print("Letter Grade=C+")
elif(Grade_points==7):
    print("Performance=Good")
    print("Letter Grade=B")
elif(Grade_points==8):
    print("Performance=Very Good")
    print("Letter Grade=B+")
elif(Grade_points==9):
    print("Performance=Excellent")
    print("Letter Grade=A")
elif(Grade_points==10):
    print("Performance==Outstanding")
    print("Letter Grade=A+")
else:
    print("error")

#-----------X------------X-------------X-----------------X------------------X-------------
#Problem 5- Write a python program to print the following pattern
# ABCDEFGHIJK
#  ABCDEFGHI
#   ABCDEFG
#    ABCDE
#     ABC
#      A

Word="ABCDEFGHIJK"

counter=1

#we first identify the pattern which says that
#we need to first leave gaps equal to (counter-1) where counter tells
#the row no. and the alphabets should decrease after every row 

while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])
    counter=counter+1

#-------------X---------------X---------------X----------------X--------------X---------------
#PROBLEM 6- Write a python script that repeatedly ask user to enter name and SID of
# students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and
# values are student’s name. Perform the following operations on Dictionary :
# a. Print students details stored in the dictionary.
# b. Sort dictionary using student names.
# c. Sort dictionary using SID.
# d. Search a student details with SID and print name of that student.

student_info=dict()
n="y"
alistsid=[]

#(a)
#here we keep a while loop that goes for infinite times
#hence it asks sid and names repeatedly and adds them to dictionary
#here i have used the if statement so that i can exit the loop whenever i want
#i am making a list along with the dictionary which will help us in further parts
print("----------------(a)-------------------")
while(n=="y"):
    sid=int(input("Give the sid (a number): \n"))
    name=input("Enter your name: \n")
    student_info[sid]=name
    n=input("give a letter y or n: \n")
    alistsid.append((sid,name))
print("The required dictionary--",student_info)
print("The list will be used in further parts--")
print("The required list--",alistsid)

#(b)
#to sort our dictionary based to names we will iterate dict.items() twice each
#time inversing the key value pair and we will form a list which can be sorted
#and converted back to dictionary hence we get the required dictionary
print("----------------(b)------------------------")
print("The dictionary we had-")
print(student_info)
#now we exchange the key value pair and make a new dictionary and a new list
newdict=dict()
alistname=[]
#now we iterate
for (k,v) in student_info.items():
    newdict[v]=k
    alistname.append((v,k))
print("now we have exchanged the key value pair but its not sorted-")
#dict and list are both not sorted
print(newdict)
print("The unsorted list--")
print(alistname)
alistname.sort()
#sorted list
print("The sorted list--")
print(alistname)
#create a sorted dictionary from our sorted list
print("The sorted dictionary-")
sorted_dict=dict(alistname)
print(sorted_dict)
# exchange the key value pair of the sorted_dict to get
#required dictionary
required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print("This is the dictionary sorted on the basis of name-")
print(required_dict_name)


#(c)
#sort the dictionary on the basis of sid
#the list we made along with dictionary will be used now
#we will first sort the list and then convert it into dictionary 
print("-----------------(c)-----------------")
print("The list we made before will be used now-")
print(alistsid)
alistsid.sort()
print("now the list is sorted-")
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print("sorted dictionary based on sid-",sorted_student_info_sid)


#(d)
#search a student's name by his/her sid
#here i will search the name of the student with key value or sid as 21103105    
print("-----------------(d)-----------------")    
entered_sid=int(input("Please enter one of the sids you entered before-\n"))
print("The name of the student with the entered sid is-\n")    
print(student_info[entered_sid])


#PROBLEM 7: Write a python program to print Fibonacci sequnce also print average of the resultant Fibbonacci series
#fibonacci sequence
first_term=int(input("Give a number-"))
second_term=int(input("Give a number-"))
#now it will keep on printing the sequence till you say y and to stop it say n
sum=first_term+second_term
series=[first_term,second_term]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to contnue and n to stop going further-")
print("Now we got a list having a fibonacci series-")
print(series)

#now lets find average of the resultant fibonacci series
sum=0
for i in series:
    sum=sum+i
print("Average of the sequence-")
print(sum/len(series))

#-------X------------X----------------X-------------X---------------X--------------
#PROBLEM 8: Given the sets below, write python statement to:
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
# a. Create a new set of all elements that are in Set1 and Set2 but not both.
# b. Create a new set of all elements that are in only one of the three sets Set1,
# Set2 and Set3.
# c. Create a new set of elements that are exactly two of the sets Set1, Set2
# and Set3.
# d. Create a new set of all integers in the range 1 to 10 that are not in Set1.
# e. Create a new set of all integers in the range 1 to 10 that are not in Set1,
# Set2 and Set3.
# Set1={1,2,3,4,5}
# Set2={2,4,6,8}
# Set3={1,5,9,13,17}

#(a)
print("-------------(a)------------")
required_Set=Set1^Set2
print(required_Set)


#(b)
print("-------------(b)------------")
required_Set=Set1^(Set2^Set3)
print(required_Set)


#(c)
print("-------------(c)------------")
required_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(required_Set)


#(d)
print("-------------(d)------------")
new_Set={1,2,3,4,5,6,7,8,9,10}
required_Set=new_Set-Set1
print(required_Set)


#(e)
print("-------------(e)------------")
required_Set=new_Set-(Set1|Set2|Set3)
print(required_Set)


    
    
    