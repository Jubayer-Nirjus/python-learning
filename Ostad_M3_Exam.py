# Q-1: 
class Student:
    def __init__(self, name="Unknown", roll_no=0):
        self.name = name
        self.roll_no = roll_no
    
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
    
    def placeholder(self):
        pass

# Testing
s1 = Student()                    
s2 = Student("John", 2)           
s1.display()
s2.display()


# Q-2:
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Name: {self.name}")

# Single Inheritance
class Student(Person):
    def show(self):  
        print(f"Student: {self.name}")

# Multilevel (Person -> Student -> GradStudent)
class GradStudent(Student):
    def show(self):
        print(f"Grad Student: {self.name}")

# Hierarchical (Person -> Teacher)
class Teacher(Person):
    def show(self):
        print(f"Teacher: {self.name}")

# Testing
s = Student("Nirjus")
g = GradStudent("Jubayer")
t = Teacher("Carol")
s.show(); g.show(); t.show() 

# Q-3: 
class Account:
    def __init__(self):
        self.__balance = 0  
    
    def get_balance(self): 
        return self.__balance
    def set_balance(self, nirjus): 
        self.__balance = nirjus
    
    def deposit(self, amt, note=None):  
        self.__balance += amt
        print(f"Deposited {amt}" + (f" ({note})" if note else ""))


class A:
    def msg(self): return "Class A"
class B:
    def msg(self): return "Class B"
class C(A, B):
    pass

# Testing
acc = Account()
acc.deposit(100)
acc.deposit(50, "Salary")

c = C()
print(c.msg())  