from collections import Counter

with open('challenge_2.txt') as challenge_2:
    contents = challenge_2.read()
    print(Counter(contents))
