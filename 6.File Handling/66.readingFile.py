# ----------------------------------------------------
#! ----------------- reading file --------------------
# ----------------------------------------------------
# ? [1] read()      --> reads entire file or specified number of characters
# ? [2] readline()  --> reads a single line or specified number of characters from a line
# ? [3] readlines() --> reads all lines as a list of strings
# ? [4] close()     --> closes the file
# ----------------------------------------------------
file = open(r"C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\adham.txt", "r")

# print(name of file.function(number of characters to read)))

print(file)  # file data object
print(file.read(5))  # read first 5 characters

print(file.read())  # read entire file content

print(file.readline(5))  # read first line
print(file.readline())  # read second line

print(file.readlines())  # read all lines as list

for line in file:
    if line.startswith("06"):
        break
    print(line)

file.close()  # close file after finishing
