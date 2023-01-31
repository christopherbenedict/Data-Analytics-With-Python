from sys import argv

if len(argv) <3:
    print ("Error, too few arguments")
elif len(argv) >4:
    print ("Error, too many arguments")
elif len(argv) ==3:
    print("This script is named {}".format(script_name))
    print("  The value of argument 1 is: {}", [0])
    print("  The value of argument 2 is: {}", [1])
    print("  The value of argument 3 is: {}", [2])

