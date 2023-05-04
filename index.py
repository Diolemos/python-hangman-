import random

word_list = ["aardvark", "baboon", "camel"]


picked_word = random.choice(word_list)


guess= input("Guess a letter").lower()
#how do I get the index? 
for word in picked_word:
    if word == guess:
        print("Do something")
    else:
        print("do something else")    
         