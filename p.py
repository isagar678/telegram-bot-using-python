import re

input = 'how are you\ ??'

input2 = re.findall(r'[\w]+',input.lower())

print(input2)