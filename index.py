import random

word_list = ["aardvark", "baboon", "camel"]


picked_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {picked_word}.')

display = []

for word in picked_word:
    display.append('_')
print(display)





# currentIndex = 0 
# for word in picked_word:
#     if word == guess:
#         display[currentIndex]= guess
#         currentIndex +=1
#     else:
#         currentIndex +=1
"While there are _, ask for words"
game_over = False

def check_not_guessed(display, underscore):
    display_str = ''.join(display)
    if display_str.find(underscore) == -1:
        return True
    
 

while not game_over:
    guess= input("Guess a letter").lower()    
    for position in range(len(picked_word)):
        letter = picked_word[position]
        if letter == guess:
            display[position]= guess
            print(display)
    game_over = check_not_guessed(display,'_')    
           
               

     
print("Hooray!")         