# Importing shit here
import os
import shutil


# Select a filename
def setting_filename():
    usr_input = input("Enter your filename: ")
    file_name = usr_input + ".py"
    print(file_name)
    return copy_create(file_name)


def copy_create(filename):
    shutil.copy("template.py", "temp.py")
    # os.chdir("C:/Users/alexa/Documents/Python/Codeacademy/")
    os.rename("temp.py", filename)


setting_filename()
