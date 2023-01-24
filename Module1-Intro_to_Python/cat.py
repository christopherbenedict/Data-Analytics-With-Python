from sys import argv
scrip,file_name = argv

file = open(file_name) #Allow you to get access to the entire file
file_content = file.read() #This reads the whole file

print(file_content) #This prints the file

file.close() #close file