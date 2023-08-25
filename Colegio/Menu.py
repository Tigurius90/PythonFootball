from Person import *
from Subject import *

#meto datos enunciado
studentList=[]
teachersList=[]
dicMarks={0:[]}

studentList.append(Person("juan","Estudiante"))
studentList[0].subjects= [Subject("Mates"),Subject("Lengua")]
studentList[0].age= 21

studentList.append(Person("Alex","Estudiante"))
studentList[1].subjects= [Subject("Mates"),Subject("Geo")]
studentList[1].age= 22

studentList.append(Person("Diego","Estudiante"))
studentList[2].subjects= [Subject("Geo"),Subject("Historia")]
studentList[2].age= 23

studentList.append(Person("Ignacio","Estudiante"))
studentList[3].subjects= [Subject("Programación"),Subject("Historia")]
studentList[3].age= 24

studentList.append(Person("Alberto","Estudiante"))
studentList[4].subjects= [Subject("Programación"),Subject("Gym")]
studentList[4].age= 25

teachersList.append(Person("Cristobal","Profesor"))
teachersList[0].subjects= [Subject("Programación")]

teachersList.append(Person("Laura","Profesor"))
teachersList[1].subjects= [Subject("Historia"),Subject("Mates")]

teachersList.append(Person("Adriana ","Profesor"))
teachersList[2].subjects= [Subject("Geo"),Subject("Lengua")]




def showStudentWithMark():
    mark=float(input("¿Que nota quieres que busque?"))
    print(set(dicMarks[mark]))
    main()


def examen(userSelectionMenu):
    global dicMarks
    uniqueListSubjects=showSubjects(userSelectionMenu)
    userSelectionSubject=(input("Escoja asignatura: "))
    for x in studentList:
        for y in x.subjects:
            if y.name ==list(uniqueListSubjects)[int(userSelectionSubject)] and y.passed==False:
                mark=float(input("Que nota ha tenido " + x.name +"?: "))
                y.marks.append(mark)
                try:
                    dicMarks[mark].append(x.name)
                except:
                    dicMarks[mark]=[x.name]
                if mark>=5:
                    y.passed=True
                else:
                    if y.suspensoCheck()==True:
                        studentList.remove(x)
    main()


def showMarks():
    c=0
    for x in studentList:
        print(str(c)+"-"+x.name)
        c +=1
    userSelection=int((input("Escoja un alumno: ")))
    print("Nota media: "+str(studentList[userSelection].meanMarks()))
    print("Nota más alta: "+str(studentList[userSelection].maxMarks()))
    print("Número de convocatorias totales: "+str(studentList[userSelection].numMarks()))
    for x in studentList[userSelection].subjects:
        if len(x.marks)>0:
            print("Estas son las notas de la asignatura "+x.name,x.marks)
            print("Esta suspenso" if x.passed==False else "Esta aprobado")
    main()

def showTeachers():
    for x in teachersList:
        print(x.dicNameSubjects())


def showTeacherStudents(uniqueListSubjects):
    userSelection=(input("Escoja opción para ver profesores y alumnos: "))
    #print(list(uniqueListSubjects)[0])
    for x in studentList+teachersList:
        for y in x.subjects:
            if y.name ==list(uniqueListSubjects)[int(userSelection)]:
                print (x.name, str(x.age) + " años" if x.role=="Estudiante" else "Profesor/a")
    main()


def showSubjects(userSelection):
    subjects_list=[]
    for x in studentList :
        for y in x.subjects:
            subjects_list.append(y.name)
    uniqueListSubjects=set(subjects_list)
    c=0
    for x in uniqueListSubjects:
        print(c,"-",x)
        c+=1
    if userSelection=="1":
        showTeacherStudents(uniqueListSubjects)
    else:
        return(uniqueListSubjects)


    

def main():
    print(" 1-Ver asignaturas \n 2-Ver profesores \n 3-Examen \n 4-Ver notas \n 5-Ver numero de nota")
    userSelection=(input("Escoja opción: "))
    if userSelection=="1":
        showSubjects(userSelection)
    if userSelection=="2":
        showTeachers()
    if userSelection=="3":
        examen(userSelection)
    if userSelection=="4":
        showMarks()
    if userSelection=="5":
        showStudentWithMark()
        

main()








