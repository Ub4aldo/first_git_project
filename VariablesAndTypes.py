#variables start with lower case letters
a =  5
b = 1.4
c = 2j
print(b, type(b))
print (a, type(a))
print (c, type(c))


d = 1j
print(d*d, type(d*d))


str = "this is string" + "this is another concat string"
print(str, type(str))

#str1  = "1"+1
#print(str1) this produces an error.


############LIST

myList = [1,2,3,4,5]
myEmptyList = []
myListOfStrings = ["a","f","f"]
myListOfList = [[1,2,3],[False, True],[]]
len(myList)


############SETS################################
mySet = {1,2,3,4,5}
type(mySet)
print(len(mySet))

mySet1={1,1,1,1,2}
print(len(mySet1))
##### the logic operators follow the algebric rules if they are applied on them####


###tuples
myTuple = 1,2,3,4
len(myTuple)
###order is important in the tuple
#### you cannot use .append with tuple context
#### the tuples are used for efficient memory reasons. Respect to the list wichi python preallocates-memory to.
#### this is the most important reason making difference btw tuple and list


#########Dictionary###############
my_dict = {"apple":"a red fruit", "pear": "yellow_fruit", "apple":"somethingelse"}
print(my_dict['apple'])
######with multiple definitions for the same keys, python will retrieve the most recent values for the repeated key.



