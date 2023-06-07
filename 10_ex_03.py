import os 
import string

file = input('Enter filename: ')


while True :
    try :
        file_handle = open( file)
        break
    except :
        print('Incorrect file path. Try again')
        file = input('Enter filename: ')
        continue

""" 
Exercise 3: 
Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies. """

#Dict to hold letters
letters_dict = dict()

#Handle string from text
for line in file_handle :
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words : 
        letters = list(word)
        for letter in letters :
            letters_dict[letter] = letters_dict.get(letter, 0) + 1
print('Dictionary of letters:')
print(letters_dict)

#store letters in tupple
letters_list = list()
for letter, count in list(letters_dict.items()) :
    letters_list.append((count, letter))

#sort letters descending
letters_list.sort(reverse=True)

print('List of letters in tupples')
#print letters and count
for count, letter in letters_list :
    print('Letter:', letter, count)