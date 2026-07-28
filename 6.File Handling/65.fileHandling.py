# ----------------------------------------------------
#! ---------------- file handling --------------------
# ----------------------------------------------------
# ? [1] "a" --> open file for appending, creates file if it does not exist
# ? [2] "r" --> [default value] open file for reading, error if file does not exist
# ? [3] "w" --> open file for writing, creates file if it does not exist, overwrites existing content
# ? [4] "x" --> open file for creating, error if file already exists
# ----------------------------------------------------
# file = open("test.txt", "a")
# name = commannd ("file name" , mode)
#               or absolute path

import os

# get current working directory
print(os.getcwd())

# get absolute path of current file
print(os.path.abspath(__file__))

# get directory of current file
print(os.path.dirname(os.path.abspath(__file__)))

# change current working directory
os.chdir(r"C:\Users\Adham\GitHub\Python-learning-path")

file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\adham.txt")
