#for inheritance problem
class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class employee(person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def display_details(self):
        return f"Name:{self.name},ID:{self.id},Salary:{self.salary}"
    
class department(person):
    def __init__(self, name, division):
        super().__init__(name,division)
        self.division = division
    def display_details(self):
        return f"Name:{self.name},Division:{self.division}"
class division(person):
    def __init__(self, name,division):
        super().__init__(name,division)
        self.division = division
    def display_details(self):
        return f"Name:{self.name}, Division:{self.division}"
      
emp1 = employee("Avanthika",101, 50000)
print(emp1.display_details())

emp2 = department("HR","Administartor")
print(emp2.display_details())

        
