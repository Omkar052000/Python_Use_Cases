import os

folders = input("Enter the folder names as a string with space as a delimeter: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please enter a valid folder name, looks like this folder does not exist: " + folder)
        continue
    except PermissionError:
        print("You do not have access to : " + folder)
        continue

    print("========= Listing files in the folder: " + folder)

    for file in files:
        print(file)


