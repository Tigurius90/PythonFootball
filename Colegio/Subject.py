class Subject:
    
    
    def __init__(self,name):
          self.name=name
          self.marks=[]
          self.practice=[]
          self.theory=[]
          self.passed=False
          self.convocatorias= 0

    
    def suspensoCheck(self):
        suspenso=0
        for x in self.marks:
            if x<5:
                suspenso +=1
        if suspenso>=3:
            print(self.name + " debe ser expulsado")
            return(True)

#ejemplo cambio para pr
