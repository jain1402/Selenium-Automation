''' Methods vs Constructor'''

''' Methods.....
    1. give any name
    2. return the values
    3. methods can take argument/parameters
    4. we have to use object to invoke the method

    Constructors.......
    1. constructor name is fixed 
            def __init__(self)
    2. constructor wil not return any value
    3. constructor can also take argument/parameters
    4. constructor will be called at the time of object creation itself
'''

# class myclass():
#     def __init__(self) -> None:
#         print("this is constructor")

# mc=myclass() # Invoke Automatically as soon as we create object

class emp():
    def __init__(self,empid,empname,empsal):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
    def display(self):
        print(self.empid,self.empname,self.empsal)
e1=emp(1,"ayush",10000000)
e1.display()
        