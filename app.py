import os

print("Welcome to Big Data Processing Application")
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
    print("take a look at localshost:8020")
if usr_val == 2:
    print("take a look at localshost:8080")
if usr_val == 3:
    print("take a look at localshost:8888")
if usr_val == 4:
    print("take a look at localshost:9000")