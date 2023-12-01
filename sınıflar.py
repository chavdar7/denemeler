"""
In this chapter we will learn the OOP, classes, objects etc. in python 
"""

class Cars:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"{self.model}:\n{self.brand} {self.model}({self.year})"
    
    
marka = input("marka giriniz: ")
model = input("model giriniz: ")
yıl = input("kaç model: ")

araba = Cars(marka, model, yıl)

