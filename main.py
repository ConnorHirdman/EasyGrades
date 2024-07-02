import json

classInfo = json.load(open('Classes.JSON'))

for i in classInfo:
    print(i["Code"])