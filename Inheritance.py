class MathStudent:
    def __init__(self,n,r,s,om,tm):
        self.name=n
        self.roll_no=r
        self.semester=s
        self.obtain_marks=om
        self.total_marks=tm

    @property
    def Subject(self):
        return 'Math'

    @property
    def Name(self):
        return self.name

    @property
    def Roll_no(self):
        return self.roll_no

    @property
    def Semester(self):
        return self.semester

    @property
    def Marks(self):
        return 100*self.obtain_marks/self.total_marks
class EngrStudent:
    def __init__(self,n,r,s,om,tm,p):
        self.name=n
        self.roll_no=r
        self.semester=s
        self.obtain_marks=om
        self.total_marks=tm
        self.practical_marks=p

    @property
    def Subject(self):
        return 'Engr'

    @property
    def Name(self):
        return self.name

    @property
    def Roll_no(self):
        return self.roll_no

    @property
    def Semester(self):
        return self.semester

    @property
    def Marks(self):
        return 70*self.obtain_marks/self.total_marks+self.practical_marks

def main():
    student=[]
    student.append(MathStudent('Hasan',14,2,78,100))
    student.append(MathStudent('Muneeb',40,2,68,100))
    student.append(EngrStudent('Navaid', 54, 3, 55, 60, 25))
    student.append(EngrStudent('Zaid', 57, 3, 45, 60, 21))
    student.append(MathStudent('Tuqeer',14,2,70,100))

    for s in student:
        print(s.Subject,end=': ')
        print(s.Name.ljust(8),end=' ')
        print(s.Roll_no,end=' ')
        print(s.Semester,end=' ')
        print(round(s.Marks,1),end=' ')
        print()
main()


