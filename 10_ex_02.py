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
Exercise 2: 
This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below. """

#Count emails and store in dictionary
hours_dict = dict()
for line in file_handle :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        nums = words[5].split(':')
        hour = nums[0]
        hours_dict[hour] = hours_dict.get(hour, 0) + 1
print(hours_dict)

#Hours dict to tupple list
hours_list = list()
for hour, count in list(hours_dict.items()) :
    hours_list.append((count, hour))

for count, hour in hours_list :
    print(hour + ':', count)