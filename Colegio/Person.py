from Subject import *
from Role import *

class Person():
    passed=False
    convocatorias=0

    def __init__(self,name,age,role,subject):
        self.name=name
        self.age=age
        self.role=role
        self.marks=[]
        self.subject=subject






    def dicNameSubjects(self):
        listSubjects=[]
        for subject in self.subjects:
            listSubjects.append(subject.name)
        print(self.name + " tiene las asignaturas " + str(listSubjects))


    def dicMarkName(self):
        dic={0:[]}
        for x in self.subjects:
            for y in x.marks:
                dic[y]=self.name
        return (dic)


    def meanMarks(self):
        allMarks=[]
        for mark in self.marks:
            allMarks.append(mark)
        print("Nota media en "+self.subject+": "+str("No tiene notas" if len(allMarks)==0 else (sum(allMarks)/len(allMarks))))

    
    def maxMarks(self):
        allMarks=[]
        for mark in self.marks:
            allMarks.append(mark)
        print("Nota más alta en "+self.subject+": "+str("No tiene notas" if len(allMarks)==0 else max(allMarks)))
    

    def numConv(self):
        allMarks=[]
        for mark in self.marks:
            allMarks.append(mark)
        print("Estas son las notas de la asignatura "+self.subject+":" +str(allMarks))
        print("Esta suspenso" if self.passed==False else "Esta aprobado")
        print("Numero de convocatorias:" +str(self.convocatorias))

    def showData(self,userSelection,uniqueListSubjects):
        for subject in self.subjects:
            if subject.name ==list(uniqueListSubjects)[int(userSelection)]:
                print (self.name, str(self.age) + " años " + str(self.role.name))

    def suspensoCheck(self):
        if self.convocatorias>3:
            print("Debe ser expulsado")
