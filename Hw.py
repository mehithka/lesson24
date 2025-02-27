class Dog:
    species = 'Animal'

    def __init__(self,name,age):
        self.name = name
        self.age = age

brain = Dog('Brain',4) 
dann  = Dog('Dann',3)

print('Brain is a {}'.format(Dog.species))
print('Dann is a {}'.format(Dog.species))

print('@Brain is a {}'.format(brain.species))
print('@Dann is a {}'.format(dann.species))

print('{} is {} years old'.format(brain.name,brain.age))
print('{} is {} years old'.format(dann.name,dann.age))