
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

""" 
Exercise 1: 

Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits. """

#Count emails and store in dictionary
email_list = dict()
for line in file_handle :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        email = words[1]
        email_list[email] = email_list.get(email, 0) + 1
#print(email_list)

#Create tuple with emails
emails_list = list()
for email, count in list(email_list.items()): 
    emails_list.append((count, email))


#Sort list of emails
emails_list.sort(reverse=True)

#Output email with most commits
for count, email in emails_list[:5]:
    print('Email:', email + " - Count:", count)