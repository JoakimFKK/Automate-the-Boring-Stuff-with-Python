import shutil, os

def creating_a_backup():
    """copytree laver en kopi af alt indholdet af en mappe og outputter det til en destination
    """
    shutil.copytree(r"C:\Users\joak\Downloads\Test", r"C:\Users\joak\Downloads\Test_Backup")

def moving_files():
    """Rykker en fil
    Filen kan også få et navneskift hvis destinationens navn bliver ændret, fx "lmao.txt"
    """
    shutil.move(r"C:\Users\DoesntExist\txt.txt", r"C:\Users\DoesntExist\thiswillnotwork\txt.txt")

def deleting_files():
    path = "location of file/directory"
    # sletter filen @ path
    os.unlink(path)
    # sletter mappen @ path, mappen skal være tom før.
    os.rmdir(path)
    # sletter mappen @ path, samt alt den indeholder
    shutil.rmtree(path)