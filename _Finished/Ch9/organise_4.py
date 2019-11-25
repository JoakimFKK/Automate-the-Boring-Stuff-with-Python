import re
import shutil
import os

date_regex = re.compile(r'''(^(.*?) # Al tekst før dato
    ((0|1)?\d)-                     # Fx. 01, 6, 10 samt bindestreg
    ((0|1|2|3)?\d)-                 # potentielt 2 digits til dato
    ((19|20)\d\d)                   # Årstal
    (.*?)$                          # Alt efter datoen.
    )''', re.VERBOSE)
    
for american_filename in os.listdir('.'):
    """Hver eneste fil blive fået igennem.
    Hvis filen ikke har et filnavn der passer med date_regex så vil resten af koden blive sprunget over
    Og den næste fil vil blive tjekket.
    """
    mo = date_regex.search(american_filename)
    if mo == None:
        continue

    before_date = mo.group(1)
    month = mo.group(2)
    date = mo.group(3)
    year = mo.group(4)
    after_date = mo.group(5)

    euro_filename = before_date + date + '-' + month + '-' + year + after_date
    abs_working_dir = os.path.abspath('.')
    new_america = os.path.join(abs_working_dir, american_filename)
    new_europe = os.path.join(abs_working_dir, euro_filename)
    print("Renaming '%s' to '%s'" % new_america, new_europe)
    # shutil.move(new_america, new_europe)