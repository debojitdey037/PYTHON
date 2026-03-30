class Student:
    collegeName = "MSOT";
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding new student to database..")


s1 = Student("debojit",89);
print(s1.name,s1.marks)
print(s1.collegeName)

