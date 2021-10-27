from collections import Counter

n = 2

with open('challenge_2.txt') as challenge_2:
    contents = challenge_2.read()
    counted = Counter(contents)
    print(Counter(contents))
