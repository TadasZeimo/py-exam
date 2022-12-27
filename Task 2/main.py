# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]


# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių

def getUserAverageAge(data):
    sum_variable = 0

    for i in data:
        sum_variable += i.get("age")

    return print(round(sum_variable / len(data), 2))


getUserAverageAge(users)

# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].
# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka


def getUsersNames(data):
    new_data = []

    for i in data:
        new_data.append(i.get("name"))

    new_data.sort()

    return print(new_data)


getUsersNames(users)
