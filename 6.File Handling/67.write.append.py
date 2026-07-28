# ----------------------------------------------------
# ! ------------ write and append in file ------------
# ----------------------------------------------------
# ? [1] write()       -->  to write in file (overrite)                "w"
# ? [2] writelines()  -->  to write multiple lines in file (overrite) "w"
# ----------------------------------------------------
file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\blabel.txt", "w")
file.write("01.Adham is the best Eng\n")
file.write("02.Adham is the best Eng\n")
file.write("03.Adham is the best Eng\n")

HList = [
    "04.Adham is the best Eng\n",
    "05.Adham is the best Eng\n",
    "06.Adham is the best Eng\n",
]
file.writelines(HList)

file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\blabel.txt", "a")
file.write("Adham is the best Eng\n" * 4)
file.write("------------------------\n")
file.write("\n\n\n\n\n\n")
file.write("------------------------\n")
