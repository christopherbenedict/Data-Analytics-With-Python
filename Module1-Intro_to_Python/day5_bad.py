from sys import argv
from os.path import exists #import object exists os.path

script, num1, num2, num2, num3, out_filename = argv #This is importing a function. 

file_exists = exsits(out_filename) # Treue if file exists False if not
print("Does the output file exist? {}".format(file_exists)) 
print("Writing output to {}".format(out_filename))

out_file = open(out_filename) #Opening out_file returning a file object
outdata = out_file # snot necesary. Defining a new variable with out_file
print("Waiting... Type the RETURN key to continue")
  input() #Allows user input
      
answer = (num1 + num2 + num2 + num3 + num4) / (len(argv) - 1)#calculating an average. len function gives us decimal points in this case 5

out_file.write("{:.2f}\n".format(answer)) #Writing the answer into out file and also formatting the number of digits in the answer that we want to print. f=float
print("\a") #Escaping a. Print alarm
out_file.close()