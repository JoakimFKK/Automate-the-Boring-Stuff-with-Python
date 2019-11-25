#! python3
# download_xkcd.py - Downloads every single XKCD comic.
import os

import bs4
import requests



def rip_xkcd_comics():
    """Alle XKCD img elementer inde i "comic" bliver downloadet og gemt.
    """
    url = 'http://xkcd.com' # Starting URL
    os.makedirs('xkcd', exist_ok=True) # Store comics in ./xkcd
    while not url.endswith('#'):
        # Download the page.
        print(f"Downloading page {url}...")
        res = requests.get(url) # Få fat i siden.
        res.raise_for_status() # Se om der er forbindelse

        soup = bs4.BeautifulSoup(res.text, 'html.parser') # Få teksten fra requests

        # Find the URL of the comic image.
        comic_elem = soup.select("#comic img") # Find img element inde i id "comic"

        # Download the image.
        if comic_elem == []: # hvis listen er tom, altså ingen img inde i "comic"
            print("Could not find comic.")
        else:
            logging.debug("Comic source bliver sat'")
            comic_src = "http:" + comic_elem[0].get('src')

            print(f"Downloading image {comic_src}...")
            res = requests.get(comic_src)
            res.raise_for_status()

            # Save the image to ./xkcd.
            # NOTE: basename tager den sidste del af en string fra en filepath, som /foo/bar/foobar.txt hvor den vil tage foobar.txt
            with open(os.path.join('xkcd', os.path.basename(comic_src)), 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)


        # Get the Prev button's url.
        prev_link = soup.select('a[rel="prev"]')[0] # Identifies the <a> element with the rel attribute set to prev.
        url = "http://xkcd.com" + prev_link.get('href')
    print("Done.")


rip_xkcd_comics()