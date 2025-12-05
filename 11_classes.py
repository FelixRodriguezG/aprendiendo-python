# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        print("Sonido genérico de animal")
 
# Instancia de la clase Animal
animal = Animal("random")       
animal.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.

class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        if self.species == "perro":
            print("Guau Guau")
        elif self.species == "gato":
            print("Miau Miau")
        else:
            print("Sonido genérico de animal")
            
dog = Animal("perro")
cat = Animal("gato")
unknown = Animal("elefante")
dog.make_sound()
            
# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
        
        
# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 10
        
    def brake(self):
        self.__speed = max(0, self.__speed - 10)  # max(0, ...) evita que la velocidad sea negativa
# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author  # propiedad privada
        
    def get_author(self):
        return self.__author
    
    def set_title(self, new_title):
        self.title = new_title
# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas  # lista de notas
        
    def calcular_nota_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


estudiante1 = Estudiante("Ana", "Perez", [8, 9, 7, 10])
print(estudiante1.calcular_nota_media())
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Fondos insuficientes o cantidad inválida.")  

bank_account = BankAccount("Carlos", 100)
bank_account.deposit(50)
print(bank_account.balance)  # Debería imprimir 150
bank_account.withdraw(30)
print(bank_account.balance)  # Debería imprimir 120
bank_account.withdraw(200)    # Debería imprimir "Fondos insuficientes o cantidad inválida."

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5  
point1 = Point(2, 3)
point2 = Point(5, 7)
print(point1.distance_to(point2))  # Debería imprimir la distancia entre point1 y point2

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.



# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.