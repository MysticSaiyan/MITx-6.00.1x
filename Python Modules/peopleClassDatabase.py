import datetime

class Person(object):
    def __init__(self, name):
        '''create person named name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    
    def getLastName(self):
        '''return self's last name'''
        return self.lastName
    
    def __str__(self):
        '''return name'''
        return self.name
    
    def setBirthday(self, month, day, year):
        '''sets birthday'''
        self.birthday = datetime.date(year,month,day)
    
    def getAge(self):
        '''returns age in days'''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        '''return true if self's name is lexicographically 
        less than the other's name, and false otherwise'''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName


class MITPerson(Person):
    nextIdNum = 0
    
    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

class Student(MITPerson):
    pass

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    
    def speak(self, utterance):
        new = "In course " + self.department + " we say "
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)



class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)
    
class Grad(Student):
    pass

class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
   
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

def gradeReport(course):
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s means grade is '
                      + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


p1 = Person("Pragun Saini")
p1.setBirthday(10,25,2000)
p2 = Person("Mark Zuckerberg")
p2.setBirthday(4,3,1984)
p3 = Person("Bill Gates")
p3.setBirthday(5,20,1965)
p4 = Person("Elon Musk")
p5 = Person("Steve Jobs")

personList = [p1,p2,p3,p4,p5]


m3 = MITPerson("Mark Zuckerberg")
Person.setBirthday(m3,5,14,1984)
m2 = MITPerson("Drew Houston")
Person.setBirthday(m2,3,4,1983)
m1 = MITPerson("Bill Gates")
Person.setBirthday(m1,10,20,1955)


MITPersonList = [m1,m2,m3]


s1 = UG("Matt Damon", 2017)
s2 = UG("Ben Affleck", 2017)
s3 = UG("Benedict Cumberbatch", 2018)
s4 = Grad("Leonardo di Caprio")

studentList = [s1,s2,s3,s4]

faculty = Professor('Doctor Arrogant', 'six')


six001 = Grades()
six001.addStudent(m2)
six001.addStudent(m3)
six001.addStudent(m1)
six001.addStudent(s1)
six001.addStudent(s2)
six001.addStudent(s3)
six001.addStudent(s4)

six001.addGrade(m2, 100)
six001.addGrade(m3, 75)
six001.addGrade(m1, 60)
six001.addGrade(s1, 84)
six001.addGrade(s2, 91)
six001.addGrade(s3, 75)
six001.addGrade(s4, 88)

print()
#print(gradeReport(six001))













