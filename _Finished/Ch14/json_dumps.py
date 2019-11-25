import json
import os

json_string = {"isCat": True, "miceCaught": 0, "name": "Zophie", "felineIQ": None}
string_of_json = json.dumps(json_string)
print(string_of_json)