file = open('myFile.txt','w')
#'w' is used to create a file if it doesn't exit yet

#to handle the file more properly we also can use try and catch as well, like
try:
    file.write('my First file')
    #to write the content inside the file
finally:
    file.close()
    #to close the file


#another way to make file in a better or short way
with open('secondFile.txt','w') as file:
    file.write('my Second file')