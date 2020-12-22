#write a program that has classes such as a student,course,department.Enroll a student in a course ofa particular department.
class student:
    def __init__(self,name,rollno,course,year):
        self.name=name
        self.rollno=rollno
        self.course=Course(course,year)
    def show(self):
        print(self.name,self.rollno)
        print(self.course.get())
class Course:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def get(self):
        return(self.name,self.year)
class dept:
    def __init__(self,name):
        self.name=name
        self.courses=[]
    def get(self):
        return(name,courses)
    def add_courses(self,name):
        self.courses.append(name)
    def show_courses(self):
        print("Courses offeres in this department are:",self.courses)
d1=dept("Mathematics")
d2=dept("Computer Science")
d1.add_courses("BA(H)")
d1.add_courses("BSc(H)")
d2.add_courses("BCA")
d2.add_courses("B.tech")
print("Dear Stuedents, the list of the courses offered are mentioned")
d1.show_courses()
d2.show_courses()
s=student("Ram",1234,"BCA",2020)
s.show()

