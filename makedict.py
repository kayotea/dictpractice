name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(lst1, lst2):
    new_dict = {}
    lstitem = 0
    if len(lst1) >= len(lst2):
        for item in lst1:
            new_dict[item] = lst2[lstitem]
    elif len(lst1) > len(lst2):
        for item in lst2:
            new_dict[item] = lst1[lstitem]

    return new_dict

make_dict(name, favorite_animal)