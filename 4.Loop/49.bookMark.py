# ----------------------------------------------------
#! ------------------- book mark ---------------------
# ----------------------------------------------------
bookMark = []
maxMark = 5

while maxMark > 0:
    website = input("Enter your favorite website URL https://")
    bookMark.append(f"https://{website.strip().lower()}")
    maxMark -= 1
    print("website added to bookmarks")
    print(f"{maxMark} left")
    print(f"Your Bookmarks:{bookMark}")
else:
    print("You have reached the maximum number of bookmarks")

if len(bookMark) > 0:
    bookMark.sort()

index = 0
while index < len(bookMark):
    print(f"{index + 1}. {bookMark[index]}")
    index += 1
