#python prgm that accepts a sentence and finds the no of words, digits, uppercase letters and lowercase letters 
import string
sen=input("Enter a sentence:")
wordList=sen.strip().split(" ")
print(f'This sentence has {len(wordList)} words',end='\n\n')

dig_count=uppercase_count=lowercase_count=0

for character in sen:
    if character in string.digits:
        dig_count+=1
    elif character in string.ascii_uppercase:
        uppercase_count+=1
    elif character in string.ascii_lowercase:
        lowercase_count+=1
print(f'Sentence has {dig_count} digits',
      f'sentence has {uppercase_count} uppercase characters',
      f'sentence has {lowercase_count} lowercase characters',sep='\n')


