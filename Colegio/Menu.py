from Person import *
from Subject import *

#meto datos enunciado
allList=[]
dicMarks={0:[]}
uniqueListSubjects=[]


DictSubjStudents={"Mates":[Person("Juan","20",Role.student,"Mates"),Person("Alex","22",Role.student,"Mates"),Person("Laura",0,Role.teacher,"Mates")]}
DictSubjStudents["Lengua"]=[Person("Juan","20",Role.student,"Lengua"),Person("Adriana",0,Role.teacher,"Lengua")]
DictSubjStudents["Geografia"]=[Person("Ignacio","23",Role.student,"Geografia"),Person("Alex","22",Role.student,"Geografia"),Person("Adriana",0,Role.teacher,"Geografia")]
DictSubjStudents["Historia"]=[Person("Ignacio","23",Role.student,"Historia"),Person("Diego","22",Role.student,"Historia"),Person("Laura",0,Role.teacher,"Historia")]
DictSubjStudents["Programacion"]=[Person("Alberto","23",Role.student,"Programacion"),Person("Diego","22",Role.student,"Programacion"),Person("Cristobal",0,Role.teacher,"Programacion")]
DictSubjStudents["Gimnasia"]=[Person("Alberto","23",Role.student,"Gimnasia")]



def showstudentWithMark():
    mark=float(input("¿Que nota quieres que busque?"))
    print(set(dicMarks[mark]))
    main()


def examen():
    global dicMarks
    showSubjects()
    userSelectionSubject=(input("Escoja asignatura: "))
    for person in DictSubjStudents[userSelectionSubject]:
            if person.passed==False and person.role==Role.student:
                mark=float(input("Que nota ha tenido " + person.name +"?: "))
                person.marks.append(mark)
                person.convocatorias += 1
                try:
                    dicMarks[mark].append(person.name)
                except:
                    dicMarks[mark]=[person.name]
                if mark>=5:
                    person.passed=True
                else:
                    person.suspensoCheck()
    main()


def showMarks():
    listStudents=[]
    for studentsSubject in DictSubjStudents.values():
        for student in studentsSubject:
            if student.role== Role.student:
                listStudents.append(student.name)
    print(list(dict.fromkeys(listStudents)))            
    userSelection=input("Escoja un alumno: ")
    for studentsSubject in DictSubjStudents.values():
        for student in studentsSubject:
            if student.name== userSelection:
                student.meanMarks()
                student.maxMarks()
                student.numConv()

    main()

def showteachers():
    listTeachers=[]
    for asignatura in DictSubjStudents:
            if DictSubjStudents[asignatura][-1].role== Role.teacher:
                teacher=DictSubjStudents[asignatura][-1].name
                listTeachers.append((teacher)) 
    print (list(dict.fromkeys(listTeachers)))
    main()


def showteacherstudents():
    userSelection=(input("Escoja opción para ver teacheres y alumnos: "))
    for person in DictSubjStudents[userSelection]:
        print(person.name +" edad "+ str(person.age)+" role "+str(person.role.name))
    main()


def showSubjects():
    print(str(DictSubjStudents.keys()))



def main():
    print(" 1-Ver asignaturas \n 2-Ver teacheres \n 3-Examen \n 4-Ver notas \n 5-Ver numero de nota")
    userSelection=(input("Escoja opción: "))
    if userSelection=="1":
        showSubjects()
        showteacherstudents()
    if userSelection=="2":
        showteachers()
    if userSelection=="3":
        examen()
    if userSelection=="4":
        showMarks()
    if userSelection=="5":
        showstudentWithMark()
        

main()








