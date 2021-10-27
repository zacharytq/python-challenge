import re

three_one_three = re.compile('[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]')

with open('challenge_3.txt') as challenge_text:
    contents = challenge_text.read()
    found_item = three_one_three.findall(contents)
    print(found_item)
