from Subject import *
from Role import *

class Person:
    name=str
    age=0
    subjects= []



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
        for x in self.subjects:
            for y in x.marks:
                allMarks.append(y)
        print("Nota media: "+str("No tiene notas" if len(allMarks)==0 else (sum(allMarks)/len(allMarks))))

    
    def maxMarks(self):
        allMarks=[]
        for x in self.subjects:
            for y in x.marks:
                allMarks.append(y)
        print("Nota más alta: "+str("No tiene notas" if len(allMarks)==0 else max(allMarks)))
    
    def numMarks(self):
        allMarks=[]
        for x in self.subjects:
            for y in x.marks:
                allMarks.append(y)
        print("Número de convocatorias totales: "+str( "No tiene notas" if len(allMarks)==0 else len(allMarks)))
    

    def numConv(self):
        for x in self.subjects:
            if len(x.marks)>0:
                print("Estas son las notas de la asignatura "+x.name,x.marks)
                print("Esta suspenso" if x.passed==False else "Esta aprobado")


    def showData(self,userSelection,uniqueListSubjects):
        for subject in self.subjects:
            if subject.name ==list(uniqueListSubjects)[int(userSelection)]:
                print (self.name, str(self.age) + " años " + str(self.role.name))

