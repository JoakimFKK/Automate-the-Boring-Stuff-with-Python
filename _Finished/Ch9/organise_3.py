import zipfile, os

def long_zip():
    """Læser og udskriver alt indholdet i en zip-fil
    """
    zip_file = zipfile.ZipFile("03_ZIP files.zip")
    for n in zip_file.namelist():
        print(n)
    # Får fat i alt info omkring filen
    spam_info = zip_file.getinfo("spam.txt")
    print(spam_info.file_size)
    print(spam_info.compress_size)
    print(f"Compressed file is {round(spam_info.file_size / spam_info.compress_size, 2)}x smaller")
    zip_file.close()

def extract_zip():
    with zipfile.ZipFile("03_ZIP files.zip") as example_zip:
        # med eller uden arguments
        example_zip.extractall("Ch9")

def extract_specific_thing_from_zip():
    with zipfile.ZipFile("03_ZIP files.zip") as dot_zip:
        dot_zip.extract("spam.txt")

def creating_zip_file():
    with zipfile.ZipFile("foobar.zip", "w") as new_zip:
        new_zip.write("Automate the Boring Stuff with Python (2015)(1).pdf", compress_type=zipfile.ZIP_DEFLATED)

def adding_to_zip_file():
        creating_zip_file()
        with zipfile.ZipFile("foobar.zip", "a") as new_zip:
                new_zip.write("files_from_book.zip", compress_type=zipfile.ZIP_DEFLATED)

