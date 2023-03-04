import re
from collections import Counter

def find_words(filename):
    list = []
    with open(filename) as f:
        text = f.read()
        words = re.findall(r'\w+', text.lower())
        for w in words:
            if (len(w) >= 6):
                list.append(w)
        return list

Words = find_words('about.txt')
MostCommon = Counter(Words).most_common(1)
print('\nThe words with atleast 6 letters and the most frequently used word is "{0}" and it is used {1} times.'.format(MostCommon[0][0], MostCommon[0][1]))