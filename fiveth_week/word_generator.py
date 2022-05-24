'''
# Разрабатываемый код
import random
# class Word_generator():
new_word = ''
unknow_word = []
with open('fiveth_week/words.txt') as f:
    words = f.readlines()
    word = random.choice(words)
    count = len(word)
    unknown_word = '_' * count
    print(unknown_word)
    print(word)
# Find a letter in word

letter = str(input('Guess a  letter (a-z): '))
if letter in word:
    list_word = list(word)
    list_word.remove('\n')
    index = word.index(letter)
    print(index)
    print(list_word)
    print('Congrats!!')
    print(f'Your letter is: {letter}')
    if not index:
         if index != 0:
             print(unknow_word[0:index])
             new_word = unknow_word[0:index] + unknow_word[index:]
    print(unknow_word[0:index] + word[index] + unknow_word[index+1:])
'''
word = ['S', 't', 'e', 'e', 'l']
new_word = ''
count = len(word)
unknow_word = '_' * count
print(unknow_word)
new_word_list = []
new_word = ''

while word != len(word):
    first_letter = str(input('Letter: '))
    index = word.index(first_letter)
    new_word_list.append(first_letter)
    word.sort()
    new_word_list.sort()
    if word == new_word_list
    #output_new_word = new_word.join(new_word_list)
    # output_new_word.sort()
# if not index:
#     if index != 0:
#         print(unknow_word[0:index])
#         new_word = unknow_word[0:index] + unknow_word[index:]
    print(unknow_word[0:index] + word[index] + unknow_word[index+1:])
    print(new_word_list)
