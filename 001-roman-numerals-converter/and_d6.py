import random

def hangman():
    word_list=["ardwark", "baboon", "camel"]
    random_word=random.choice(word_list)
    
    list=[]
    for elements in range (0,len(random_word)):
        list += "_"
    guess = input("Guess a letter: ").lower
   
    game =True    
    while game  :
        for i in list:
            if i =="_":
                for indexNo in range(0,len(random_word)):
                    letter = random_word[indexNo]
                    if letter==guess:
                        list[indexNo]=letter
                    print(list)
                    if "_" not in list:
                        game=False
                        print("Game is Over")
                           
                                   

hangman() 



