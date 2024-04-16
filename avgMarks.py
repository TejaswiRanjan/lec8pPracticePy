# Create student class that takes name & marks of 3 students as arguments in constructor Then create a method to print the average

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def printAvg(self):
        avg = 0
        for num in self.marks:
            avg = avg + num
        
        print("The name is ", self.name)
        print("The average marks is ", avg/3)

s1 = Student("Tejaswi",[99,94,96])
s1.printAvg()
