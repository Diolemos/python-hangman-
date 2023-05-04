import random

word_list = ["aardvark", "baboon", "camel"]


picked_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {picked_word}.')

display = []

for word in picked_word:
    display.append('_')
print(display)

guess= input("Guess a letter").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
indexes = []
# how do I get the index? 
currentIndex = 0 
for word in picked_word:
    if word == guess:
        display[currentIndex]= guess
        currentIndex +=1
    else:
        currentIndex +=1
           

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.         
print(display)         