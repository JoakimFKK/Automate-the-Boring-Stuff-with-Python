"""NUVÆRENDE PROBLEMER:
<div class="r">
    <a href="søgeresultat_url"> EKSISTERE IKKE INDE I SOUP.

Hvad der bliver modtaget fra requests og hvad der er i selve browseren er anderledes.
"""

import sys
import webbrowser

import bs4
import requests

def do_you_feel_lucky(search_query):
    print("Googling...") # Display text.
    # res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])) # "[url]?q= [sysarv input]"
    google_query = 'http://google.com/search?q=' + search_query
    res = requests.get(google_query) # "[url]?q= [sysarv input]"
    res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Open a browser tab for each result.
    """Hvert søgeresultat er inde i en div med classen 'r', hvor resultatet selv er af elementet 'a'."""
    link_elems = soup.select('.r a')
    print(len(link_elems))

    num_open = min(4, len(link_elems)) # 4, ellers lændgen af link_elems, hvilket returnere den mindste værdi.
"""     for i in range(num_open):
        webbrowser.open('http://google.com' + link_elems[i].get('href'))
 """

if __name__ == "__main__":
    query = input("Please input a search query: ")
    do_you_feel_lucky(query)
    # do_you_feel_lucky("github")
    