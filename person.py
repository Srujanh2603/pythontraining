class person(object):
    def __init__(self,name,idno):
        self.name = name
        self.idno = idno
    def display(self):
        print(self.name)
        print(self.idno)
    def details(self):
        print(f'My name  is {self.name}')
        print(f'My id is {self.idno}')
    
class employee(person):                                   #inherited class 
    def __init__(self,name,idno,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idno)
    def display(self):
        print(f'My name is {self.name}')
        print(f'My id is {self.idno}')
        print('Post is :{}'.format(self.post))

a=employee('Rahul',886012,20000,'Intern')
a.display()
a.details()