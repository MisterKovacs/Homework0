

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if new_floor <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break

    def __str__(self):
        return f'"Название: {self.name}, кол-во этажей: {self.number_of_floors}"'

    def __len__(self):
        return self.number_of_floors


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
print()
h2.go_to(10)
print()

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)
#str
print(h3)
print(h4)
print()
#len
print(len(h3))
print(len(h4))



