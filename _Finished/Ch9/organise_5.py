"""back_to_zip copies an entire folder and its content into a zipfile whose name increments.
"""
import zipfile
import os

def back_to_zip(folder):
    folder = os.path.abspath(folder)
    no_file = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(no_file) + '.zip'
        # Hvis zip_filename eksistere, incrementer.
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the zip file.
    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        # FIXME Don't pick up every single folder.
        for foldername, subfolders, filenames in os.walk(folder):
            print(f"Adding files in {foldername}...")
            backup_zip.write(foldername)
            for filename in filenames:
                new_base = os.path.basename(folder) + '_'
                if filename.startswith(new_base) and filename.endswith('.zip'):
                    continue
                backup_zip.write(os.path.join(foldername, filename))



back_to_zip(os.path.dirname(os.path.realpath(__file__))) # Hvor filen er placeret.