"""A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result."""
#example of function
def Greet(name):
    print("Hello", name)

"""Greet("John")  # Output: Hello John
Greet("Cynthia")
Greet("David")
Greet("Davis")"""

#function to add two numbers
def AddTwoNumbers(Number1,Number2):
   
    print(Number1+Number2) 
AddTwoNumbers(45,10)

print (AddTwoNumbers(90,3))   #Output :8

def Name(*names):
    print("the name is " + names[4])



#Name('sasa', 'were', 'david', 'john', 'Cynthia')


#javascript function Greet{console.log("Hello" + name)};
    
#write a function that returns only even numbers in a list

def Even_numbers(Our_list):
    for i in  Our_list:
        if i % 2 == 0:
            print(i)

Even_numbers([1,2,3,6,7,8,9,10,12,4]) # we the output to be 2,6,8,10 and 12
    