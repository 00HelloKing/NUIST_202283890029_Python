# Add Two Numbers in Python
# Author: Jin Kaifeng
# Using a function

# function to add two numbers
def add(a,b):
  # converting input to float and adding
  result = float(a) + float(b)
  return result

# taking user input
a = input("First number: ")
b = input("Second number: ")

# calling function
res = add(a,b)
print("The Answer is: ")
print(res)
