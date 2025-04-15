# zadanie 1


import math



class LogExp:
    
    def __init__(self,a=None):
        self.a = a
        
        
    def Log(self,x):
        return math.log(x,self.a)
        
        
    def Potega(self,x):
        return self.a**x 
    
licz = LogExp(10)

print(licz.Potega(3))
print(licz.Log(100))
        
# Zadanie 2

# class Prostokąt:
    
#     def __init__(self,a=None,b=None):
#         self.a = a
#         self.b = b
    
#     def Pole(self):
#         return self.a*self.b
    

# class Kwadrat(Prostokąt):
    
#     def Pole(self):
#         return self.a**2
    
    
# pros = Prostokąt(3,7)

# print(pros.Pole())

# kwad = Kwadrat(6)

# print(kwad.Pole())


# Zadanie 3

# class Student:
    
#     def __init__(self, imię = None, nazwisko = None, indeks = None):
#         self.imię = imię
#         self.nazwisko = nazwisko
#         self.indeks = indeks
        
#     oceny = {
#             "Matematyka" : None,
#             "Polski" : None,
#             "Angielski" : None
#         }
        
   
    
    
# def WypiszOceny(oceny):
#     for i in oceny:
#         print(oceny)
                
                
# oceny = {
#             "Matematyka" : None,
#             "Polski" : None,
#             "Angielski" : None
#         }
# uczen = Student

# WypiszOceny(oceny)

# Zadanie 4

class Employee:
    
    def __init__(self,first_name = None, last_name = None, annual_salary = None):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def given_raise(self, bonus = 2000):
        self.annual_salary += bonus
    
    given_raise()

emp = Employee("Imie","Nazwisko",4300) 

print(emp.annual_salary)  