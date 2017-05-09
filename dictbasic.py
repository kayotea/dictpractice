from collections import OrderedDict

anna = OrderedDict()
anna['name'] = 'Anna'
anna['age'] = 45
anna['species'] = 'alien'
anna['birthplace'] = 'Pacific Ocean'
anna['occupation'] = 'spy'

def printPerson(person):
    for key in person:
        print key, ":",person[key]

printPerson(anna)