from logging import root


class student(object):
    def __init__(self,name,rollNo):
        self.name=name
        self.rollno=rollNo
# creating class exam

class exam(student):
    def __init__(self,name,rollNo,marks):
        super().__init__(name,rollNo)
        self.marks=marks
        
#creating class result  

class result(exam):
    def __init__(self, name,rollNo,marks):
        super().__init__(name,rollNo,marks)
        self.resultt=marks
        self.total_marks=self.resultt/600*100
        self.percentage=self.total_marks
     
    def display(self):
        return self.percentage

s=result("neel",1,500)
print(s.display())
