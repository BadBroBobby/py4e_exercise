""" txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)

print("-".join(res))

# Code: http://www.py4e.com/code3/soft.py """

directory = dict()

directory['Vandborg','Chris'] = 61785120
directory['Christensen', 'Kristine'] = 27509868

#The expression in brackets is a tuple. We could use tuple assignment in a for loop to traverse this dictionary.

for last, first in directory:
    print(first, last, directory[last,first])