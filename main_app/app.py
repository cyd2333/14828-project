import os

raw_input("Welcome to big data processing toolbox!")
print("Please type the number that corresponds to which application you would like to run:")
print("1. Apache Hadoop")
print("2. Apache Spark")
print("3. Jupyter Notebook")
print("4. SonarQube and SonarScanner")
print("")

usr_val = input("Type the number here:  ")
usr_app = ""

# error checking
if type(usr_val) != int:
    raise RuntimeError
if usr_val >=5 or usr_val <= 0:
    raise RuntimeError

# generate url for different app 
if usr_val == 1:
    print("take a look at 34.82.144.7:9870")
if usr_val == 2:
    print("take a look at 35.199.188.103:8080")
if usr_val == 3:
    print("take a look at 34.83.32.126:8888")
if usr_val == 4:
    print("take a look at 34.145.106.105:9000")