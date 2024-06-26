#A Class is like an object constructor, or a "blueprint" for creating objects.
class StudentDetails:
    def __init__(self, name, regno, age, grade):
        self.name = name  # instance variable
        self.regno = regno  
        self.age = age
        self.grade = grade

    # def __str__(self):
    #     return f"{self.name}, {self.age}"
    #     pass
    def DisplayGreeting(self):
        print ('hello my name is ',self.name )

Student1 = StudentDetails('were','bsclmr178221', 20, 80)
Student2 = StudentDetails('David', 'bsclm33421', 20, 78.5)
# print(f"name : ", Student2.name, "admission number: ", Student2.regno)
# print(Student1)
# Student1.DisplayGreeting()
# Student2.DisplayGreeting()

class StudentScores:
    def __init__(self, score1, score2, score3, score4):
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4
    
    def ScoreAvarage(self):
        total = self.score1 + self.score2 + self.score3 + self.score4
        print(total/4) 

Student1 = StudentScores(34.5,67,89,70)
Student2 =StudentScores(70,70,70,70)
Student2.ScoreAvarage()

""" 1. create a an object called Vehicle, the attributes of the vehicle includes, brake, wheel, fuel,vehicletype, then print out hte details of thevehicle
2. StudentScore, write a function within the class to get the product of the scores

"""
# Inheritance allows us to define a class that inherits all the methods and properties \n 
#from another class. This means we can create new classes based on  existing ones. \n

class Person:
    def __init__(self,first_name, last_name):
        self.first_name =first_name
        self.last_name = last_name

    def PrintNames(self):
        print(self.first_name, self.last_name)

person1= Person('Davis', 'Were')
person2 = Person("David", "Oludare")
person1.PrintNames()

# Create a class named Student, which will inherit the
# properties and methods from the Person class:
class Student(Person):
    def __init__(self, first_name, last_name, regno):
        super().__init__(first_name, last_name)
        self.regno= regno
student1= Student("kombo", 'joseph', 'bsclmrw33445')
print(student1.first_name,  student1.last_name,student1.regno)

class  Employee(Person): #Employee is derived from person
    pass

employee1 = Employee("John","Doe")
# print(employee1.first_name)
employee1.PrintNames()



