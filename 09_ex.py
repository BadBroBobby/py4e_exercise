""" 
Exercise 1: 

Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary. """

""" import os 

file = input('Enter filename: ')
# Få den aktuelle sti til 08_ex.py-filen
current_dir = os.path.dirname(os.path.abspath(__file__))

# Konstruer stien til materials-mappen baseret på den aktuelle sti
materials_dir = os.path.join(current_dir, "../materials")

# Tilgå filen i materials-mappen
file_path = os.path.join(materials_dir, file)

file_handle = open( file_path) """

""" words_list = dict()
for line in file_handle :
    line.rstrip()
    words = line.split()
    for word in words :
        if word in words_list : continue
        else : words_list[word] = 1
print(words_list) """

""" 
Exercise 2: 
Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter). """

""" import os 

file = input('Enter filename: ')
# Få den aktuelle sti til 08_ex.py-filen
current_dir = os.path.dirname(os.path.abspath(__file__))

# Konstruer stien til materials-mappen baseret på den aktuelle sti
materials_dir = os.path.join(current_dir, "../materials")

# Tilgå filen i materials-mappen
file_path = os.path.join(materials_dir, file)

while True :
    try :
        file_handle = open( file_path)
        break
    except :
        print('Incorrect file path. Try again')
        file = input('Enter filename: ')
        # Få den aktuelle sti til 08_ex.py-filen
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Konstruer stien til materials-mappen baseret på den aktuelle sti
        materials_dir = os.path.join(current_dir, "../materials")

        # Tilgå filen i materials-mappen
        file_path = os.path.join(materials_dir, file)
        continue

email_day = dict()
for line in file_handle :
    line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        word = words[2]
    email_day[word] = email_day.get(word, 0) + 1

print(email_day) """

""" import os 

file = input('Enter filename: ')
# Få den aktuelle sti til 08_ex.py-filen
current_dir = os.path.dirname(os.path.abspath(__file__))

# Konstruer stien til materials-mappen baseret på den aktuelle sti
materials_dir = os.path.join(current_dir, "../materials")

# Tilgå filen i materials-mappen
file_path = os.path.join(materials_dir, file)

while True :
    try :
        file_handle = open( file_path)
        break
    except :
        print('Incorrect file path. Try again')
        file = input('Enter filename: ')
        # Få den aktuelle sti til 08_ex.py-filen
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Konstruer stien til materials-mappen baseret på den aktuelle sti
        materials_dir = os.path.join(current_dir, "../materials")

        # Tilgå filen i materials-mappen
        file_path = os.path.join(materials_dir, file)
        continue

email_count = dict()
for line in file_handle :
    line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        word = words[1]
    email_count[word] = email_count.get(word, 0) + 1

print(email_count)
 """
""" 
Exercise 4: 
Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has. """

""" max_email_count = None
max_email = None
email_list = list(email_count.items())
for key, value in email_list:
    if max_email_count is None or value > max_email_count:
        max_email_count = value
        max_email = key

print('Most mails received from:', max_email)
print('Emails received:', max_email_count) """

""" 
Exercise 5: 
This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary. """

import os 

file = input('Enter filename: ')
# Få den aktuelle sti til 08_ex.py-filen
current_dir = os.path.dirname(os.path.abspath(__file__))

# Konstruer stien til materials-mappen baseret på den aktuelle sti
materials_dir = os.path.join(current_dir, "../materials")

# Tilgå filen i materials-mappen
file_path = os.path.join(materials_dir, file)

while True :
    try :
        file_handle = open( file_path)
        break
    except :
        print('Incorrect file path. Try again')
        file = input('Enter filename: ')
        # Få den aktuelle sti til 08_ex.py-filen
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Konstruer stien til materials-mappen baseret på den aktuelle sti
        materials_dir = os.path.join(current_dir, "../materials")

        # Tilgå filen i materials-mappen
        file_path = os.path.join(materials_dir, file)
        continue

email_count = dict()
for line in file_handle :
    line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        email = words[1]
        email_split = email.split('@')
        domain = email_split[1]
    email_count[domain] = email_count.get(domain, 0) + 1

print(email_count)
print('Domain list:')
emails_list = list(email_count.items())
for k, v in emails_list :
    print(k , '-', v)
