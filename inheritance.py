class Animal:
    def __init__(self):
        self.name = "Dog"
        
    def bark(self):
        self.age = 2
        print(self.age)
        
class Lab(Animal):
    
    def __init__(self):
        super().__init__()
        self.names = "Dogs"
    
    def bark(self):
        super().bark()
        self.age = 3
        print(self.age)

doggs = Lab()
doggs.bark()
print(doggs.name)
print(doggs.names)