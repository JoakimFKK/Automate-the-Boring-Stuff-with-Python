#! python3
import requests
import os
import bs4
import threading

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.makedirs('Workfiles/xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):
    """Rækkefølge på events:
        Downloading af siden
        Tjek hvis der er fejl.

        Læs HTML-siden og put det i et objekt.
        Find img elementet der er inde i et element med "comic" som ID

        Hvis der ikke er nogle elementer, så sker der ingenting.
        Hvis der er, så tag det første element, og få 'src' teksten (img url), og sæt "http:" først.
        Download comic src url, tjek for fejl, og download det i chunks
        
        Arguments:
            start_comic {int} -- Start comic nummer der startes på
            end_comic {int} -- Hvor downloadingen slutter
    """
    for url_number in range(start_comic, end_comic):
        # # download the page
        # print(f'Downloading page http://xkcd.com/{url_number}')
        res = requests.get(f'http://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print("Could not find comic image.")
        else:
            comic_src = "http:" + comic_elem[0].get('src')
            # download the image
            print(f"Downloading image {comic_src}...")
            res = requests.get(comic_src)
            res.raise_for_status()

            # Save the image to the folder
            with open(os.path.join('Workfiles/xkcd', os.path.basename(comic_src)), 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)

# Create and start the thread objects
download_threads = [] # A list of all thread objects
for i in range(0, 1400, 100): # Loops 14 times, creates 14 threads
    """Every thread will look like this:
        download_xkcd(0, 99)
        The next one will be (100, 199)
    """
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end
for download_thread in download_threads:
    download_thread.join()
print("\nDone!")