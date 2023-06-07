import re

""" 
counter = 0
hand = open('mbox.txt')
for line in hand: 
    line = line.rstrip()
    if re.search('From:', line):
        words = line.split()
        for word in words :
            if re.search('@', word) :
                email = word
                counter += 1
print('First', counter)

counter = 0
hand = open('mbox.txt')
for line in hand: 
    line = line.rstrip()
    if re.search('^F..m:.+@', line):
        words = line.split()
        for word in words :
            if re.search('@', word) :
                email = word
                counter += 1
print('Second', counter) 
"""
#Searching text for emails
hand = open('mbox-short.txt')
lst = list()
for line in hand :
    lst = lst + re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)

print('Emails:')
for email in lst :
    print(email)

#Searching text for spam confidence
hand = open('mbox-short.txt')
spam_list = list()
for line in hand :
    spam_list = spam_list + re.findall('^X-.*: ([0-9.]+)', line)

print('Spam confidences:')
for email in spam_list :
    print(email)

# Search for lines that start with 'Details: rev='
# followed by numbers
# Then print the number if one is found
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print(x)
