# ----------------------------------------------------
#! ----------------- while loop ----------------------
# ----------------------------------------------------
theList = ["adham", "ahmed", "yasser", "mahmoud", "ali", "mohamed"]

i = 0
while i < len(theList):
    print(f"{str(i+1).zfill(2)}. {theList[i]}")
    print(f"{i+1:02d}. {theList[i]}")
    i += 1
