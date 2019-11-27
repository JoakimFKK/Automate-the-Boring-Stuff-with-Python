from PIL import Image
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def working_with_img_data_type():
    catIm = Image.open('zophie.png')
    print(catIm.size) # (816, 1088) == Width = 816, Height = 1088
    width, height = catIm.size # 816 1088
    print(width, height)
    print(catIm.format_description) # Portable network graphics
    catIm.save('zophie.jpg')

def creating_new_image():
    img = Image.new('RGBA', (500, 1000), 'purple')
    img.save('purpleImage.png')
    tran_img = Image.new('RGBA', (500, 1000))
    tran_img.save('transparentImage.png')

# cropping images
def cropping_images():
    catIm = Image.open("zophieCrop.png")
    cropped_img = catIm.crop((335, 345, 565, 560))
    cropped_img.save('bodylessZophie.png')

# copying and pasting images onto other images
def copying_and_pasting_images_onto_other_images():
    """NOTE:
    Note that the past() method modifies its Image object in place; it does not return an image object with the pasted image.
    If you want to call paste() but also keep an untouched version of the original image around, you'll need to first copy the image and then call paste() on that copy.
    """
    catIm = Image.open('zophie.png')
    catCopyIm = catIm.copy()

    faceIm = Image.open('bodylessZophie.png')

    catCopyIm.paste(faceIm, (0, 0))
    catCopyIm.paste(faceIm, (400, 500))
    catCopyIm.save('pasted.png')

def say_you_want_popart_of_zophie():
    catIm = Image.open('zophie.png')
    faceIm = Image.open('bodylessZophie.png')
    cat_width, cat_height = catIm.size
    face_width, face_height = faceIm.size
    catCopyIm = catIm.copy()
    # Start value, value to stop at, jump
    for left in range(0, cat_width, face_width):
        for top in range(0, cat_height, face_height):
            print(left, top)
            catCopyIm.paste(faceIm, (left, top))

    catCopyIm.save('tiledZophie.png')


def resizing_an_image():
    catIm = Image.open('zophie.png')
    width, height = catIm.size
    quarter_sized_img = catIm.resize(((int(width / 2)), (int(height / 2 ))))
    quarter_sized_img.save('quarterzophie.png')
    svelte_img = catIm.resize((width, height + 300))
    svelte_img.save('svelte.png')

def rotating_and_flipping_images():
    catIm = Image.open('zophie.png')
    catIm.rotate(90).save('rotated90.png')  # Size 816, 1088
    catIm.rotate(180).save('rotated180.png') # Size 816, 1088
    catIm.rotate(270).save('rotated270.png') # Size 816, 1088
    
    catIm.rotate(6).save('rotated6.png') # Size 816, 1088
    catIm.rotate(6, expand=True).save('rotated6_expanded.png') # Size 926, 1168

    catIm.rotate(90, resample=Image.NEAREST, expand=True).save('rotated90_pillow.png') # Size 1088, 816
    catIm.rotate(90, expand=True).save('rotated90_pillow2.png') # Size 1088, 816

    catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

def changing_individual_pixels():
    im = Image.new('RGBA', (100, 100))
    print(im.getpixel((0, 0))) # (0, 0, 0, 0)
    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210))

    from PIL import ImageColor
    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

    print(im.getpixel((0, 0))) # (210, 210, 210, 255)
    print(im.getpixel((0, 50))) # (169, 169, 169, 255)
    im.save('putPixel.png')