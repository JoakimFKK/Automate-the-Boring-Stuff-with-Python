import requests # pip install

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
# You can tell that the request for this web page succeeded by checking the status_code attribute of the response object.
# If it is equal to the value of requests.codes.ok then everything went fine.
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])


# Checking for errors.
res_fail = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res_fail.raise_for_status()
except Exception as exc:
    print(f"There was a problem: {exc}")