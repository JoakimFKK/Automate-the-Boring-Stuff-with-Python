import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

json_string = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
json_data_to_python = json.loads(json_string)

print(json_data_to_python)