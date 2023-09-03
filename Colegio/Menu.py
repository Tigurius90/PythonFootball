from Person import *
from Subject import *

#meto datos enunciado
allList=[]
dicMarks={0:[]}
uniqueListSubjects=[]

allList.append(Person())
allList[0].name="Juan"
allList[0].subjects= [Subject("Mates"),Subject("Lengua")]
allList[0].age= 21
allList[0].role=Role.student


allList.append(Person())
allList[1].name="Alex"
allList[1].subjects= [Subject("Mates"),Subject("Geo")]
allList[1].age= 22
allList[1].role=Role.student

allList.append(Person())
allList[2].name="Diego"
allList[2].subjects= [Subject("Geo"),Subject("Historia")]
allList[2].age= 23
allList[2].role=Role.student

allList.append(Person())
allList[3].name="Ignacio"
allList[3].subjects= [Subject("Programación"),Subject("Historia")]
allList[3].age= 24
allList[3].role=Role.student

allList.append(Person())
allList[4].name="Alberto"
allList[4].subjects= [Subject("Programación"),Subject("Gym")]
allList[4].age= 25
allList[4].role=Role.student

allList.append(Person())
allList[5].name="Cristobal"
allList[5].subjects= [Subject("Programación")]
allList[5].role=Role(1)

allList.append(Person())
allList[6].name="Laura"
allList[6].subjects= [Subject("Historia"),Subject("Mates")]
allList[6].role=Role(1)

allList.append(Person())
allList[7].name="Adriana"
allList[7].subjects= [Subject("Geo"),Subject("Lengua")]
allList[7].role=Role(1)





def showstudentWithMark():
    mark=float(input("¿Que nota quieres que busque?"))
    print(set(dicMarks[mark]))
    main()


def examen(userSelectionMenu):
    global dicMarks
    showSubjects()
    userSelectionSubject=(input("Escoja asignatura: "))
    for x in allList:
        for y in x.subjects:
            if y.name ==list(uniqueListSubjects)[int(userSelectionSubject)] and y.passed==False and x.role==Role.student:
                mark=float(input("Que nota ha tenido " + x.name +"?: "))
                y.marks.append(mark)
                y.convocatorias += 1
                try:
                    dicMarks[mark].append(x.name)
                except:
                    dicMarks[mark]=[x.name]
                if mark>=5:
                    y.passed=True
                else:
                    if y.suspensoCheck()==True:
                        allList.remove(x)
    main()


def showMarks():
    for c, x in enumerate(allList):
        print(str(c)+"-"+x.name)
    userSelection=int((input("Escoja un alumno: ")))
    allList[userSelection].meanMarks()
    allList[userSelection].maxMarks()
    allList[userSelection].numMarks()
    allList[userSelection].numConv()


    main()

def showteachers():
    for person in allList:
        if person.role==Role.teacher:
            print(person.dicNameSubjects())


def showteacherstudents():
    userSelection=(input("Escoja opción para ver teacheres y alumnos: "))
    #print(list(uniqueListSubjects)[0])
    for student in allList:
        student.showData(userSelection,uniqueListSubjects)
    main()


def showSubjects():
    global uniqueListSubjects
    subjects_list=[]
    for x in allList :
        for y in x.subjects:
            subjects_list.append(y.name)
    uniqueListSubjects=set(subjects_list)
    for c, x in enumerate(uniqueListSubjects):
        print(c,"-",x)



    

def main():
    print(" 1-Ver asignaturas \n 2-Ver teacheres \n 3-Examen \n 4-Ver notas \n 5-Ver numero de nota")
    userSelection=(input("Escoja opción: "))
    if userSelection=="1":
        showSubjects()
        showteacherstudents()
    if userSelection=="2":
        showteachers()
    if userSelection=="3":
        examen(userSelection)
    if userSelection=="4":
        showMarks()
    if userSelection=="5":
        showstudentWithMark()
        

main()








