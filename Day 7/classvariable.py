i,j = 20,30       # Global variable
class myclass():
    a,b = 100,200 # Class Variable
    def add(self,a,b):
        print (a+b) # Local variable
        print (self.a + self.b)
        print (i +j)

mc=myclass()
mc.add(1,2)

# Exaample :1 One class can have multiple objects

class myclass():
    def display(self,name):
        print("this is display")
        print (name)

mc1=myclass()
mc1.display("Ayush")

mc2=myclass()
mc2.display("jain")

