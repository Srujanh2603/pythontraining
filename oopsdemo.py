class bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot fly")
        
class sparrow(bird):
    def flight(self):
        print("Sparrow can fly")
        
class ostrich(bird):
    def flight(self):
        print("Ostrich cannot fly")
        
obj_bird=bird()
obj_sparrow=sparrow()
obj_ostrich=ostrich()
obj_bird.intro()
obj_bird.flight()
obj_sparrow.intro()
obj_sparrow.flight()
obj_ostrich.intro()
obj_ostrich.flight()

class super:
    var1=None #public data member
    _var2=None #protected data member
    __var3=None #private data member
    
    
    #Constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3
    
    
    #public member function
    def displaypubitems(self):
        print("Public data member",self.var1)
        
    #protected member function
    def _displayproitems(self):
        print("Protected data member",self._var2)
        
    #private member function
    def __displaypriitems(self):
        print("Private data member",self.__var3)
    
    def accesspriitems(self):
        self.__displaypriitems()
        
class sub(super):
    def __init__(self,var1,var2,var3):
        super.__init__(self,var1,var2,var3)
        
    def accessproitems(self):
        self._displayproitems()
        
obj=sub("Hello","all","people")

obj.displaypubitems()
obj.accessproitems()
obj.accesspriitems()

print("Object is accessing protected data member:",obj._var2)
