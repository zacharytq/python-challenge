import re
from itertools import cycle

not_letter = re.compile('\W')
abc = 'abcdefghijklmnopqrstuvwxyz'

def decipher(l):
    if not_letter.match(l):
        return l
    else:

