"""
This file performs adds and subtracts input numbers. 

Author: Dr. Stephen Ficklin

This file can be used by anyone after they have paid $1,000,000 for it.
   
"""

class MyNumber:
"""
    This class stores a number and performs basic mathematics on the input number.
    
    Attributes
    ----------
    x : int
        The number that this class works with.

    Methods
    -------
    print():
        Prints the number    
    add(y):
        Adds the number in y to the number of this object.
    subtract(y):
        Subtacts the number in y to the number of this object.
    """
    def __init__(self, x):
        if not type(x) == int:
            raise Exception("Please provide an integer when using the MyNumber object")
        self.x = x
  """
    This function intiations the process and asks user to confirm that a integer is needed.

    """     
        
    def print(self):
        print("The number is: {}".format(self.x))
"""
    This function prints the input number.
   
    Returns
    -------
    print
        prints the statement with the input number

    """        
    
    def add(self, y):
        self.x = self.x + y
"""
    This function adds the numbers.
   Parameters
    ----------  
    self: integer
    
    Returns
    -------
    returns added numbers
"""
    
    def subtract(self, y):
        self.x = self.x - y
"""
    This function subtracts the numbers.
   Parameters
    ----------  
    self: integer
    
    Returns
    -------
    returns subtracted numbers 
  
"""

def main():
    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()

"""
    This function outputs the numbers.
   Parameters
    ----------  
    xval: integer
    yval: integer
    
    Returns
    -------
    computes and prints output 
  
"""
if __name__ == "__main__":
    main()