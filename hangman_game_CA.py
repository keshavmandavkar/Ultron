import random
f = open("cities.txt","r")
data = f.readline()
word_list = data.split()

#Select a random word

word = random.choice(word_list).upper()
total_chances = 7
guessed_word = "-" * len(word)
guessed_letters = []  

# Hangman stages
hangman_stages = [
    """
    +----+
    |    |
         |
         | 
         |
         |
         |
    ========    
    """,
    """
    +----+
    |    |
    o    |
         |
         |
         |
         |
    ========        
    """,
    """
    +----+
    |    |
    o    |
    |    |
         |
         |
         |    
    ========
    """,
    """
    +----+
    |    |
    o    |
   /|    |
         |
         |
         |    
    ========
    """,
    """
    +----+
    |    |
    o    |    
   /|\   |
         |
         |
         |    
    ========
    """,
    """
    +----+
    |    |
    o    |
   /|\   |
   /     |
         |
         |    
    ========
    """,
    """
    +----+
    |    |
    o    |
   /|\   |
   / \   |
         |
         |    
    ========
    """

]

# Welcome message
print("Welcome to Hangman!")
print("You have 7 chances to guess the word correctly. Let's begin!\n")

# main loop
while total_chances > 0:
    print(guessed_word)
    print(hangman_stages[7 - total_chances])  # Show the hangman figure based on chances left
    print("Guessed letters:", " ".join(guessed_letters))  # Show guessed letters
    letter = input("Guess a letter: ").upper()
    if letter in guessed_letters:
        print("You have already guessed '{letter}' . Try another one.")
    guessed_letters.append(letter)    

    

    if letter in word:
        print(f"Good guess! The letter {letter} is in the word.\n")
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]

        if guessed_word == word:
            print("\nCongratulations!! You have won!")
            print("The word was:", word)
            break
    else:
        total_chances -= 1
        print(f"Oops! The letter {letter} is not in the word.\n")
        print(f"Remaining Chances: {total_chances}\n")

    if total_chances == 0:
        print("Game over! The word was: " + word + ". Better luck next time!")
        print(hangman_stages[6])  # Shows complete hangman

print("\nThanks for playing!")
