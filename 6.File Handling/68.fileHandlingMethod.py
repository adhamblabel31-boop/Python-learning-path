# ----------------------------------------------------
# ! ----------------- file handling ------------------
# ----------------------------------------------------
# ? truncate()  -->  to remove content from specific position
# ? tell()      -->  to get current position of pointer
# ? seek()      -->  to move pointer to specific position
# ? remove()    -->  to delete a file
# ----------------------------------------------------

file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\adham.txt", "a")
# file.truncate(8)  # delete all content after 8 characters

file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\adham.txt", "a")
print(file.tell())  # get current position of pointer
#todo# new line = two characters (\r\n)

file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\adham.txt", "a")
file.seek(3)  # move pointer to specific position
print(file.tell())  # get current position of pointer
# print(file.read())  # read from current position

import os

os.remove(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\Blabel.txt")
