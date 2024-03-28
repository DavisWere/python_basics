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
    