"""Creates _.bak, _.dat, and _.dir files that stores variables
"""
import shelve
import pprint

def shelve_the_long_way():
    shelf = shelve.open('Ch8 Reading and Writing\\mydata')
    text = ["hello", "world", "goodbye"]
    shelf['text'] = text
    shelf.close()

def shelve_looking_good():
    with shelve.open('Ch8 Reading and Writing\\mydata') as shelf:
        numb = [420, 69, 1776]
        shelf['numb'] = numb

def get_shelves():
    with shelve.open("Ch8 Reading and Writing\\mydata") as shelf:
        print(list(shelf.keys()))
        print(list(shelf.values()))

def peepee_print():
    cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
    pprint.pformat(cats)