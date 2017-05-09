students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#receive student array of dicts containing first/lastname
def printStudents(studs):
    for i in range(len(studs)):
        print studs[i]['first_name'],studs[i]['last_name']

printStudents(students)

print '.'

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#given a dictionary of arrays containing dicts
#print in a format
def printUsers(users):
    chars = 0
    firstname = ''
    lastname = ''
    for key in users:
        print key
        for i in range(len(users[key])):
            firstname = users[key][i]['first_name']
            lastname = users[key][i]['last_name']
            for letter in firstname:
                chars += 1
            for letter in lastname:
                chars += 1
            print i,"-", firstname.upper(),lastname.upper(),"-",chars

printUsers(users)