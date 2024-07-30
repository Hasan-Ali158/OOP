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
    sub1 = EnSubject("ILI-123","DLD",3,80)
    sub2 = EnSubject("LMN-161","OOP",3,90)
    a = Student("BSDSF23A000","Fahad","2",[sub1,sub2])
    print(a)
    b = Student("BSDSF23A000","Uzair","2",[sub1,sub2])
    print(b)
    c = Student("BSDSF23A000","Saad","2",[sub1,sub2])
    d = Student("BSDSF23A000","MK","2",[sub1,sub2])
    print(c)
    print(d)
    data = [a,b,c,d]
    file = open("studs.pkl","wb")
    pickle.dump(data,file)
    file.close()
main()
