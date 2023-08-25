from Subject import *

class Person:
    def __init__(self,name,role):
        self.role=role
        self.name=name
        self.age=0
        self.subjects= []
        self.suspensos=0
    def dicNameSubjects(self):
        for x in self.subjects:
            listSubjects=x.name
        return ({self.name:listSubjects})






