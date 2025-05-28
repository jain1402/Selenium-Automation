'''class ---> collection of Variables & methods
   object --> object is an instance of class
   For one class we can create multiple objects
   objects are independent

   Feartures in oops
   1. Class
   2. object
   3. Method
   4. constructor
   5. Inheritance
   

   2 Types of methods we can define within the class
   a. instance method (we can call only through objects)
   b. static method ( we can directly call using class ) annotaion is @staticmethod 

'''

# class myclass():
#     def mym1(self,a,b):
#         print (a,b)

# mc=myclass()
# mc.mym1(10,20)
# print(mc)

class mycls():
    def mym2(self):
        print("this is instance method")
    @staticmethod
    def mym3(self,num):
        print(self,num)

# mc1=mycls()
# mc1.mym2
# mc1.mym3(100,200)

mycls.mym3(10,20)