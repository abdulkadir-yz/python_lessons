# # def printname(name):
# #     print("Hello " + name)
# # __name__= "Anoj"
# # printname(__name__)

# def printname(name):
#     print("Kadir ")

# result = printname("Kadir")
# print(result)

class Car:
    def __init__(self, brand=None, model=None, year=None):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.year} {self.brand} {self.model}") 
my_car = Car("Toyota" )
my_car.start()