
#list comprhension
from turtle import clear


mylist = [1,2,3,4,5]
print([2 * item for item in mylist])

#list comprehension with filter
mylist = list(range(100))
filteredList = [item for item in mylist if item % 10 == 0]
print(filteredList)

#list comprehension with function and inpacking
mystring = "isndoaindioas aosidnaosind. aoidnaoinda doiasndoa dioandoais doai daoi da."
print(mystring.split())

def cleanworld(world):
    return world.replace('.','').lower()

print([cleanworld(world) for world in mystring.split()])

#the comprehensioin gives to python code the dub of beign pythonic code.
# With dictionary can we do the same sorcery 
animalsList = [('a','ardvak'),('b','bear'),('c','cat'),('d','dog')]
animals = {item[0]:item[1] for item in animalsList}
#print(animals)
animals = {key : value for key, value in animalsList}
#print(animals)
#elegant unpacking and wrapping
print([{'letter':key, 'name':value} for key, value in animals.items()])