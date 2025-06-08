myMap = {'name': 'Alex','age': 28,'occupation':'Business Man'}

#to access specific value
print(myMap['name'])
#by using get method
print(myMap.get('age'))

#to change specific value
myMap['name'] = 'Mike'
print(myMap)

#printing map using for loop
for keys in myMap:
    print(keys,myMap[keys])


#another method of printing values and keys for loop
for key,value in myMap.items():
    print(keys,value)

#using if condition to check the elements in our dictionary
if 'name' in myMap:
    print('[name]key is include in our map')

#add another element in our map
myMap['major'] = 'Marketing'

#to remove specific element from our map
myMap.pop('major')
print(myMap)

#to remove the last element
print(myMap.popitem())
print(myMap)

#we also have delete option as well to delete specific element
del myMap['name']
print(myMap)

#dictionary of square numbers
squared_num = {x:x**2 for x in range(6)}
print(squared_num)

#clear method to delete the whole map
squared_num.clear()
print(squared_num)

#another way to make dictionary
my_keys = ['Lemon','Ginger','Green']
default_val = 'Tea'

my_dictionary = dict.fromkeys(my_keys,default_val)
print(my_dictionary)

#we also add the values at the same time
books_keys = ['Motivational','Fictional']
books_dict = dict.fromkeys(books_keys,'book')
print(books_dict)


