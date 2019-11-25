import send2trash as trash
"""Send2trash sletter ikke filerne permenent, i modsætning til shutil og os
"""

with open("send2trash.txt", "a") as txtfile:
    txtfile.write("hello world")
trash.send2trash("send2trash.txt")