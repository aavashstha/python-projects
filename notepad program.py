import shutil
import os

if not os.path.exists("C:/Users/aavas/OneDrive/Desktop/text_folder"):
    os.makedirs("C:/Users/aavas/OneDrive/Desktop/text_folder")

text_folder = "C:/Users/aavas/OneDrive/Desktop/text_folder"

content = ""
file_name = ""
append = ""

print()
print("********** NOTEPAD **********")
print()
while True:
    file_name = input("Name the text file: ")
    name, extension = os.path.splitext(file_name)
    if extension != "":
        print("Please write the file_name without any extension!!!")
        continue
    elif os.path.exists(text_folder + "/" + file_name + ".txt"):
        print("You already have a file with this name!!!")
        while True:
            append = input("Do you want to append over this file? (Y or N): ").upper()
            if append not in ("Y", "N"):
                print("Please enter a valid respose (Y or N)!!!")
                continue
            else:
                break
        break
    else:
        break


file_name += ".txt"

if append == "":
    print()
    content = input("Enter your text content:\n")
    print()
    with open(file_name, "w") as file:
        file.write(content)
    try:
        shutil.move(file_name, text_folder)
        print(f"The text file '{file_name}' was successfully created!")
    except Exception as e:
        print(f"Can't complete the operation! Error: {e}")
        
elif append == "Y":
    with open(text_folder + "/" + file_name, "r") as file:
        prev_content = file.read()
        print(f"The file's consisting content:\n{prev_content}")
    print()
    content = input("Enter your text content:\n")
    print()
    try:
        with open(text_folder + "/" + file_name, "a") as file:
            file.write(content)
        print(f"Successfully appended the content to the '{file_name}'")
    except Exception as e:
        print(f"Can't append content to the file! Error:{e}")
elif append == "N":
    print("Operation Cancelled!")