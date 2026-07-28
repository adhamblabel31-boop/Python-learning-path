# ----------------------------------------------------
# ! -------------- image with pillow -----------------
# ----------------------------------------------------
from PIL import Image

# open image
myLogo = Image.open(r"C:\Users\Adham\GitHub\Python-learning-path\7.Extras\logo.jpg")

# show image
myLogo.show()

# crop image
cropLogo = (100, 100, 1000, 1000)
#            L ,  U ,   R ,   D
croppedLogo = myLogo.crop(cropLogo)

# show cropped image
croppedLogo.show()

# convert mode
convertLogo = myLogo.convert("L")
convertLogo.show()
