import random
import art
import hangman_words

print(art.logo)
picked_word = random.choice(hangman_words.word_list)
#Testing code
# print(f'Pssst, the solution is {picked_word}.')

display = []

for word in picked_word:
    display.append('_')
print(display)

# "While there are _, ask for words"

user_lives = 6

game_over = False


    
 

while not game_over:
    guess= input("Guess a letter: ").lower() 
    if guess in display:
        print(f"You have already guessed that letter.")   
    for position in range(len(picked_word)):
        letter = picked_word[position]
        if letter == guess:
            display[position]= guess
            print(display)
            
       
    if guess not in picked_word:
        user_lives -= 1
        print("Sorry, no such letter")
        art.hangman_list[user_lives  ]()   #print hangman
    if  user_lives == 0:
        game_over = True  
        print("At least you tried")
    
    if '_' not in display:
        game_over = True
        print("You is grate wordsmith!")
       
            
      
                 
             
                
            
                

      
      
           
               

     
        