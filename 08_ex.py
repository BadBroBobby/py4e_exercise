#Exercises
print('Hello World!')

""" 
Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order. 
"""
""" import os 
file = input('Enter filename: ')
# Få den aktuelle sti til 08_ex.py-filen
current_dir = os.path.dirname(os.path.abspath(__file__))

# Konstruer stien til materials-mappen baseret på den aktuelle sti
materials_dir = os.path.join(current_dir, "../materials")

# Tilgå filen i materials-mappen
file_path = os.path.join(materials_dir, file)

file_handle = open( file_path) """

""" unique_words = list()
for line in file_handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word in unique_words : continue
        else :
            unique_words.append(word)

unique_words.sort()
print(unique_words)
print('Number of unique words:', len(unique_words)) """

""" 
Exercise 5: Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which stores emails consecutively. Emails are separated by a special line which starts with From (notice the space). Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed: """

""" email_counter = 0
emails = list()
for line in file_handle :
    line = line.rstrip()
    if not line.startswith('From '): continue
    email = line.split()[1]
    email_counter = email_counter + 1
    emails.append(email)
    print(email)

print('There were', email_counter, 'lines in the file with From as the first word')
emails.sort()
print(emails) """

""" 
Exercise 6: 

Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes. """

numbers = list()
while True :
    number = input('Please write a number. Write "done" to end: ')
    if number.lower() == 'done' : break
    try :
        number = int(number)
    except :
        print('Please write a proper number or "done" to end.')
        continue
    numbers.append(number)

print('Numbers list:', numbers)
print('Largest number:', max(numbers))
print('Smallest number:', min(numbers))
