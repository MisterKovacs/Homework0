
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor +1):
            if new_floor <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break

    def __str__(self):
        return f'"Название: {self.name}, кол-во этажей: {self.number_of_floors}"'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return f'Введены некорректные данные'
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return f'Введены некорректные данные'
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            return f'Введены некорректные данные'



print('ЗАДАНИЕ 5.1: ')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print()
print('--------------------------------')
print('Задание 5.2:'.upper())

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)
#str
print(h3)
print(h4)
#len
print(len(h3))
print(len(h4))

print()
print('--------------------------------')
print()

print('ЗАДАНИЕ 5.3: ')

print(h3)
print(h4)

print(h3 == h4)  # __eq__

h3 = h3 + 10  # __add__
print(h3)
print(h3 == h4)

h3 += 10  # __iadd__
print(h3)

h4 = 10 + h4  # __radd__
print(h4)

print(h3 > h4)  # __gt__
print(h3 >= h4)  # __ge__
print(h3 < h4)  # __lt__
print(h3 <= h4)  # __le__
print(h3 != h4)  # __ne__
