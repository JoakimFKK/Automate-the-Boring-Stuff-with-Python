import bs4  # beautifulsoup4 PIP INSTALL BEAUITULFULSOUP4
import requests

""" Download with beautifulsoup """
# region

# res = requests.get('http://google.com')
# res.raise_for_status()
# google = bs4.BeautifulSoup(res.text)
# print(type(google))  # <class 'bs4.BeautifulSoup'>

# endregion

"""Loading an HTML file with beautifulsoup"""
# region

# example_file = open('example.html')
# example_soup = bs4.BeautifulSoup(example_file)
# print(type(example_soup))  # <class 'bs4.BeautifulSoup'>

# endregion

"""Finding an element with the select() method"""
#region Finding an element with the select() method

# region !!NEEDED!!

# example_file = open('example.html')
# soup = bs4.BeautifulSoup(example_file.read(), "html.parser")
# author_elements = soup.select('#author')

# endregion

#region Prints examples

# print(type(author_elements))  # <class 'list'>
# print(len(author_elements))  # 1
# print(type(author_elements[0]))  # <class 'bs4.element.Tag'>
# print(author_elements[0].getText())  # Al Sweigart
# print(str(author_elements[0]))  # <span id="author">Al Sweigart</span>
# print(author_elements[0].attrs)  # {'id': 'author'}

#endregion

#region Print examples multiple elements

# p_elems = soup.select('p')
# print(str(p_elems[0])) # # <p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>
# print(p_elems[0].getText())  # Download my Python book from my website.
# print(str(p_elems[1]))  # <p class="slogan">Learn Python the easy way!</p>
# print(p_elems[1].getText())  # Learn Python the easy way!
# print(str(p_elems[2]))  # <p>By <span id="author">Al Sweigart</span></p>
# print((p_elems[2].getText()))  # By Al Sweigart

#endregion

#endregion Finding an element with the select() method

"""Getting data from an element's attributes"""
#region GETTING DATA FROM AN ELEMENT'S ATTRIBUTES

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
span_elems = soup.select('span')[0]
print(str(span_elems)) # <span id="author">Al Sweigart</span>
print(span_elems.get('id')) # author
print(span_elems.get('some_nonexistent_addr') == None) # True 
print(span_elems.attrs) # {'id': 'author'}

#endregion GETTING DATA FROM AN ELEMENT'S ATTRIBUTES
