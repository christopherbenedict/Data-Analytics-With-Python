from sys import argv
scrip,file_name = argv

file = open(file_name) #Allow you to get access to the entire file
file = open(copy_file, "w")

file_content = file.read() #This reads the whole file

copy_file.write(file_content) #This prints the file

file.close() #close file