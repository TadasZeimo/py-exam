# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


def showObjectKeys(data):
    new_data = []
    
    for i in data.values():
        new_data.append(i)

    return print(new_data)


showObjectKeys(audi)
