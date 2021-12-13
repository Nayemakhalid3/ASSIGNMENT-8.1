
import os


# 1
directory = input("Please enter the name of directory or path in which you want to save your file!\n")


# 2
filename = input("Please enter the file name in which you want to save your data(without extension)!\n")


# 3
if not os.path.exists(directory):
    os.makedirs(directory)
    print("The directory or path successfully created!\n")
else:
    print("The directory or path already exists!\n")


# 4
name = input("Enter your name: ")
address = input ("Enter your address: ")
phone = input ("Enter your phone number: ")

data = name + ", " + address + ", " + phone + "."

with open(f"{directory}/{filename}.txt", "w") as text_file:
    text_file.write(data)

print("The data is written to your profile successfully...\n")



# 5
readData = ''
with open(f"{directory}/{filename}.txt") as file:
    for line in file:
        readData = readData + line.rstrip()

print("Please validate the data: ")
print(f"\n{readData}")

