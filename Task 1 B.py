import pickle
class Subject:
    def __init__(self,code, subname, credit):
        self.code = code
        self.subname = subname
        self.credit = credit
    def __str__(self):
        return f"{self.code}, {self.subname}, {self.credit}"
class EnSubject(Subject):
    def __init__(self,code,subname,credit,marks):
        super().__init__(code,subname,credit)
        self.marks = marks
    def __str__(self):
        return f"{self.code}, {self.subname}, {self.credit}, {self.marks}"
class Student:
    def __init__(self,roll, name, sem, subjects):
        self.roll = roll
        self.name = name
        self.sem = sem
        self.subjects = subjects
    def __str__(self):
        sr = f"{self.roll}, {self.name}, Semester : {self.sem}\nEnrolled Subjects : \n"
        for subject in self.subjects:
            sr += str(subject) + "\n"
        return sr
def main():
    file = open("studs.pkl","rb")
    data = pickle.load(file)
    file.close()
    for student in data:
        print(student)
main()
