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


