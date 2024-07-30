class Course:
    def __init__(self,code,title, credit, sem, _type):
        self.code = code
        self.title = title
        self.credit = credit
        self.sem = sem
        self.type = _type
    def __str__(self):
        return f"{self.code.ljust(10)}{self.title.ljust(40)}{self.credit.ljust(5)}{self.sem.ljust(5)}{self.type}"
def main():
    courses = []
    options =["a","s","d","l","e","q"]
    while True:
        print("a) Add  s)Search  d)Delete  l)List All  e)Edit   q)Quit")
        x = input()
        if x not in options:
            print("Invalid Option")
            continue
        if x == "q":
            break
        elif x=="a":
            code = input("Enter Course Code :")
            title = input("Enter Course Title :")
            credit = input("Enter Credit Hours :")
            sem = input("Enter Semester :")
            tp = input("Enter Course Type :")
            courses.append(Course(code,title,credit,sem,tp))
        elif x=="l":
            if len(courses) == 0:
                print("No Courses")
            else:
                header = "Code      Title                                   Crd  Sem  Type"
                print(header)
                for course in courses:
                    print(course)
        elif x=="d":
            if len(courses) == 0:
                print("No Courses to Delete")
            else:
                a = int(input("Enter Index to Delete :"))
                try:
                    courses.pop(a)
                except:
                    print("Index Not Found")
        elif x=="s":
            a = input("Enter Search Material : ")
            for course in courses:
                if a in course.__str__():
                    print(course)
        elif x=="e":
            a = int(input("Enter index you want to edit : "))
            code = input("Enter Course Code :")
            title = input("Enter Course Title :")
            credit = input("Enter Credit Hours :")
            sem = input("Enter Semester :")
            tp = input("Enter Course Type :")
            try:
                courses[a] = Course(code,title,credit,sem,tp)
            except:
                print("Index Not Found")
    xfile = open("courses.txt","w")
    header = "Code      Title                                   Crd  Sem  Type\n"
    xfile.write(header)
    for i in range(len(courses)):
        xfile.write(courses[i].__str__())
    xfile.close()
main()
