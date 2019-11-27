from PIL import Image
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# capital variable names to indicate it's a constant
LOGO_FILENAME = 'catlogo.png'
SQUARE_FIT_SIZE = 300
LOGO_PERCENTAGE = 0.10
logo_img = Image.open(LOGO_FILENAME)  # open the catlogo.png as an Image object
logo_width, logo_height = logo_img.size
logo_width = int(LOGO_PERCENTAGE * logo_width) # resizing cat logo with easily adjustable percentage
logo_height = int(LOGO_PERCENTAGE * logo_height)
resized_logo_img = logo_img.resize((logo_width, logo_height)) # Image object that will be changed.
for filename in os.listdir(): # loop over the strings returned from os.listdir('.')
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    img_obj = Image.open(filename)
    width, height = Image.open(filename).size # get the width and height of the image from the size attribute
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
    resized_img_obj = img_obj.resize((width, height))
    resized_img_obj.paste(resized_logo_img, ((width - logo_width), (height - logo_height)), resized_logo_img)
    resized_img_obj.save(f"Workfiles/resized_{filename}")