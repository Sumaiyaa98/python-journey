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


# we also have open('file','r') option as well which is used to read the file
#  Why do we use with open('youtube.txt', 'r') as file:?
# 'r' means read mode.

# You use it when you just want to read the contents of a file.

# This will not create the file if it doesn’t exist — instead, it will give an error.

# 📌 What’s the difference between 'r' and 'w'?
# Mode	What It Does
# 'r'	Read file — file must exist or you'll get an error (FileNotFoundError).
# 'w'	Write to file — if the file doesn’t exist, Python will create it. If it does exist, Python will overwrite it.