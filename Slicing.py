name = "My names is Ubaldo Bucci"

print(name[0]) #first character Rminder: indexes starts from zero in python
print(name[1]) #second character
print(name[0:7]) #characts up to 7th

print(name[:7]) #as before
print(name[11:]) #start slicing from the end of the string


#####Formatting############
print(f"my number is {5}")
print(f"my number is {5} and it times 2 is {2*5}")

#################multi-line string with triple quotes feature##############
myString = '''here is a long text of code
i can add multiple line of coding ina stringaosdnoaifa
aodaondo
asodnaoi'''

print(myString)



mylist = [1,2,3,4,5,4,5,4,5] #list with duplicates
print(set(mylist)) #how to remove them

#in the set you cannot use slicing and other subscripting base access because the ordeer is irrelevant.
#to appen element to the set you have .toss it inside. basically is like an .append




def returnmultiplevariables():
    return 1,2,3

print(type(returnmultiplevariables()))

#### unpacking values procedure#######
a,b,c = returnmultiplevariables()
print(a,b,c)