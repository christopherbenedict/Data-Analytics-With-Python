pythionfrom sys import argv
from os.path import exists #import object exists os.path

script, num1, num2, num5, num3, num4, out_filename = argv #This is importing a function. 

file_exists = exists(out_filename) # True if file exists False if not
print("Does the output file exist? {}".format(file_exists)) 
print("Writing output to {}".format(out_filename))

out_file = open(out_filename, 'w') #Opening out_file returning a file object
outdata = out_file # snot necesary. Defining a new variable with out_file
print("Waiting... Type the RETURN key to continue")
  input() #Allows user input
      
answer = (float(num1) + float(num2) + float(num2) + float(num3) + float(num4) / (len(argv) - 1))#calculating an average. len function gives us decimal points in this case 5

out_file.write("{:.2f}\n".format(answer)) #Writing the answer into out file and also formatting the number of digits in the answer that we want to print. f=float
print("\a") #Escaping a. Print alarm
out_file.close()