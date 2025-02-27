class Parrot:
    sepcies = 'bird'

    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = Parrot('blu',10)
woo = Parrot('woo',5)

print('blu is a {}'.format(blu.sepcies))
print('woo is a {}'.format(woo.sepcies))

print('{} is {} years old'.format(blu.name,blu.age))
print('{} is {} years old'.format(woo.name,woo.age))