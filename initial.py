"""print("welcome to python class")
# adding numbers
print(1+2) # 3"""
"""num1 = 566778
num2 =45678
results = num1 + num2
print(results)"""

StudentName = "davis"
Student, Name, grades = "davis", "were", 30
# datatypes
#string - str
# number - int  float complex
# list   tuple set dictionary bool NoneType

is_male  = True
age      = 29
height  = 1.75
weight  = 65.5
eye_color= 'Brown'

# print(type(eye_color))
#list - Lists are used to store multiple items in a single variable.
MyList= ['bmw', 'audi','toyota','lexus','v8', 'benz',2 ,4,6,8,7,9,0, False, 'hello']
#print(len(MyList))
#indexing starts from 0
MyList[7]= "Mercedes"
# if 4 in MyList:
#     print('item is present')
# else:
#     print('item not available')
#print(MyList)
#print(MyList[1:7])
#print(type(MyList))
#user input 
# Name = input("Enter your name: ")
# Age = int(input("How old are you? :"))
# # print("My name is  ", Name)
# print("I am ", Age," years old.")

StudentName = 'Davis Were' # str
StudentClass = 'Computer Science'
StudentGrade = 80.5 # type float
StudentAge = 18 # type int
StudentAdmissionNumber = 'bsclmr178221'
# print(StudentName, StudentClass, StudentGrade, StudentAdmissionNumber)
# print(type(StudentName))

# def GreaterNumber(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# print(GreaterNumber(7,4,6))

def GreaterNumber(num1,num2,num3):
    if num1> num2 and num1>num3:
        return num1
    elif  num2>num1 and num2>num3:
        return num2
    else: 
        return num3
    
# print(GreaterNumber(100,56,91))

# use of  / and %   operator

print(4/2)
print(4%2) # output is  0,   because the division result is an integer
          # so there is no remainder left to find out
print(10//3) # this will give us the quotient only , it does not show any decimal places
            # even though the actual answer has a decimal part
print(10%3) # this gives us the remainder after dividing the number by another number
             # in this case we get 1 as the output because the remainder is one