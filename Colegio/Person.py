from Subject import *

class Person:
    def __init__(self,name,role):
        self.role=role
        self.name=name
        self.age=0
        self.subjects= []
        

    def dicNameSubjects(self):
        for x in self.subjects:
            listSubjects=x.name
        return ({self.name:listSubjects})


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
        return "No tiene notas" if len(allMarks)==0 else (sum(allMarks)/len(allMarks))
    
    def maxMarks(self):
        allMarks=[]
        for x in self.subjects:
            for y in x.marks:
                allMarks.append(y)
        return "No tiene notas" if len(allMarks)==0 else max(allMarks)
    
    def numMarks(self):
        allMarks=[]
        for x in self.subjects:
            for y in x.marks:
                allMarks.append(y)
        return "No tiene notas" if len(allMarks)==0 else len(allMarks)

