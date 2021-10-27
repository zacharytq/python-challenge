import re
from itertools import cycle, islice

not_letter = re.compile('\W')
abc = 'abcdefghijklmnopqrstuvwxyz'


def decipher(l):
    if not_letter.match(l):
        return l
    else:
        ind = abc.find(l) + 3
        return list(islice(cycle(abc), ind))[-1]


