from PIL import ImageColor as imagecolor
# PIL = pillow

print(imagecolor.getcolor('red', 'RGBA')) # (255, 0, 0, 255)
print(imagecolor.getcolor('RED', 'RGBA')) # (255, 0, 0, 255)
print(imagecolor.getcolor('Black', 'RGBA')) # (0, 0, 0, 255)
print(imagecolor.getcolor('chocolate', 'RGBA')) # (210, 105, 30, 255)
print(imagecolor.getcolor('CornflowerBlue', 'RGBA')) # (100, 149, 237, 255)