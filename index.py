import random

word_list = ["aardvark", "baboon", "camel"]


picked_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {picked_word}.')

guess= input("Guess a letter").lower()
#how do I get the index? 
for word in picked_word:
    if word == guess:
        print("right")
    else:
        print("wrong")    
         