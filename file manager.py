import shutil
import os

if not os.path.exists("C:/Users/aavas/OneDrive/Desktop/pdf_folder"):
    os.makedirs("C:/Users/aavas/OneDrive/Desktop/pdf_folder")
if not os.path.exists("C:/Users/aavas/OneDrive/Desktop/image_folder"):
    os.makedirs("C:/Users/aavas/OneDrive/Desktop/image_folder")

pdf_folder = "C:/Users/aavas/OneDrive/Desktop/pdf_folder"
image_folder = "C:/Users/aavas/OneDrive/Desktop/image_folder"

while True:
    file_location = input("Enter the file location: ")


    if "\\" in file_location:
        file_location = file_location.replace("\\", "/")
    
    name, extension = os.path.splitext(file_location)
    extension = extension.lower()
        

    if extension == ".pdf":
        if not os.path.isfile(file_location):
            print("There is no such file location!!!")
            continue
        else:
            file_type = "pdf"
            break
    elif extension in (".png", ".jpg", ".jpeg"):
        if not os.path.isfile(file_location):
            print("There is no such file location!!!")
            continue
        else:
            file_type = "img"
            break
    else:
        print("Please enter a valid file path of a pdf or img file!!!")
        continue


if file_type == "pdf":
    try:
        shutil.move(file_location, pdf_folder)
    # except shutil.Error:
    #     print("The file already exists in the pdf_folder!")
    except Exception as e:
        print(f"Can't move the pdf file! Error: {e}")
elif file_type == "img":
    try:
        shutil.move(file_location, image_folder)
    except shutil.Error:
        print("The file already exists in the image_folder!")
    except Exception as e:
        print(f"Can't move the pdf file! Error: {e}")

