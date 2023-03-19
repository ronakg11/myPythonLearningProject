import json

courses = '{"name": "Ronak Gavandi", "languages": ["Java", "Python"]}'
dict_courses = json.loads(courses)
list_courses = dict_courses["languages"][0]
# print(list_courses)
print(list_courses)
