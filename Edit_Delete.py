import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.txt'):
            print(root+'/'+str(file))

file_name = str(input("Write your file name: "))
# Read file.txt
print("\nWrite your option with a number: \n")
option = 
with open(file_name, 'r+') as file:
    strings = file.read().splitlines()
    print(strings)
    Del = str(input('Enter the word you would like to delete: '))
    strings.remove(Del)
    if Del in strings:
        file.writelines(Del)
        print(strings)

# Delete text and Write
#with open(edit, 'w') as file:
#    word = str(input("Write the string to delete: "))
#    # Delete all content
#    word = text.insert(word, '')
#    new_word = str(input("Write your new string: "))
#    # Write
#    file.write(new_word)

#with open(file_name, 'r+') as f:
#    file = f.readlines()
#    file.insert(0,'Freelancer.com\n')
#    f.seek(0)
#    f.writelines(file)
    
    
#with open(file_name, 'w') as f:
#    Del = str(input('Enter the word you would like to delete: '))
#    for Del in strings:
#        strings.remove(Del)
#        print(strings)
#        f.writelines(strings+"\n")
        
