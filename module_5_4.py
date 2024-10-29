class House:  # созданный класс(Hause)
    houses_history = []  # для модуля 5.4 создан атрибут внутри класса, будет хранить названия(name) объектов
    def __new__(cls, *args, **kwargs):   # метод(__new__) переопределяет методы класса, обращается(cls) на сам класс
        cls.houses_history.append(args[0])   # добавляем(append) в атрибут класса значение (*args)
        return super().__new__(cls)     # метод(super) возвращает ссылку на созданный объект в классе

    def __init__ (self, name, number_of_floors):  # метод(__init__) это конструктор, в нем создаются основные атрибуты
        self.name = name  # атрибут1 - название дома(Hause)
        self.number_of_floors = number_of_floors   # атрибут2 - количество этажей дома

    def go_to (self, new_floor):   # метод(goto) это переход(лифт) от 1 этажа до указанного значения(new_floor)
        self.new_floor = new_floor    # атрибут принимаемый значение при вызове функции(go_to)

        if new_floor >= self.number_of_floors or new_floor <= 1:   # условие1 внутри метода(go_to) сравнивает атрибуты из разных методов
            print("Такого этажа не существует")    # надпись если условие выполняется

        else:   # условие2 при котором перебирается принятое значение с первого элемента и выводится на печать, последовательно
            for i in range(1, new_floor + 1):
                print(i)

# модуль 5.2
    def __len__(self):  # метод(__len__) возвращает количество символов в строке, всегда целое число
        return self.number_of_floors  # возвращает количество этаже

    def __str__(self):  # метод(__str__) возвращает строковое представление
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # возвращает строку

# модуль 5.3
    # метод(__eq__) сравнивает два атрибута(количество этажей в зданиях), возвращает self
    def __eq__(self, other):
        return self.number_of_floors == other

    # метод(__lt__) сравнивает два атрибута(количество этажей в зданиях), возвращает self
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    # метод(__le__) сравнивает два атрибута(количество этажей в зданиях), возвращает self
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    # метод(__gt__) сравнивает два атрибута(количество этажей в зданиях), возвращает self
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    # метод(__ge__) сравнивает два атрибута(количество этажей в зданиях), возвращает self
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    # метод(__ne__) сравнивает два атрибута(количество этажей в зданиях), возвращает self
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    # метод(__add__) используется для определения поведения оператора сложения (+), возвращает новое значение (сумма двух)
    def __add__(self, value):
        # функция(isinstance()) проверяет, является ли объект экземпляром указанного класса или его подкласса
       if isinstance(value, int):
            self.number_of_floors += value
            return self

    # метод(__radd__) определяет поведение оператора сложения, когда один атрибут не имеет метода __add__
    def __radd__(self, value):
        self.__add__(value)
        return self    # достаточно прописать "return self.__add__(value)"

    #  # метод(__iadd__) возвращает метод __add__
    def __iadd__(self, value):
        self.__add__(value)
        return self     # достаточно прописать "return self.__add__(value)"

    def __del__(self):
        print(self.name, "снесён, но он останется в истории")



# для модуля 5.1
# h1 = House('ЖК Горский', 18)  # добавление переменной1 в класс(Hause), с присвоением двух значений
# h2 = House('Домик в деревне', 2)   # добавление переменной2 в класс(Hause)
# print(h1.name, h1.number_of_floors)   #вызов переменной класса с атрибутами метода(__init__)
# print(h2.name, h2.number_of_floors)
# h1.go_to(5)   # вызов метода(go_to) с присвоением значения(на како этаж надо)
# h2.go_to(10)

# # для модуля 5.2
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(str(h1))
# print(str(h2))
#
# # __len__
# print(len(h1))
# print(len(h2))

# для модуля 5.3
#
# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__

# для метода 5.4

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
