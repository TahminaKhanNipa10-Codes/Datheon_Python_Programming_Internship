import random
import os


HANGMAN_PICS = [
    r'''
       +---+
           |
           |
           |
          ===''', r'''
       +---+
       O   |
           |
           |
          ===''', r'''
       +---+
       O   |
       |   |
           |
          ===''', r'''
       +---+
       O   |
      /|   |
           |
          ===''', r'''
       +---+
       O   |
      /|\  |
           |
          ===''', r'''
       +---+
       O   |
      /|\  |
      /    |
          ===''', r'''
       +---+
       O   |
      /|\  |
      / \  |
          ==='''
]

def load_words():
    
    try:
        with open('words.txt', 'r') as file:
            
            words = [line.strip().upper() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print("words.txt file not found! Using default words...")
        return ['DATHEON', 'PYTHON', 'DEVELOPER', 'SOFTWARE', 'INTERNSHIP']

def play_hangman():
    words = load_words()
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6
    
    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print(HANGMAN_PICS[6 - attempts_left])
        
        display_word = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("\nWord: ", " ".join(display_word))
        print(f"Attempts left: {attempts_left}")
        
        if '_' not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return
            
        guess = input("Guess a single letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            attempts_left -= 1
            print("Incorrect guess!")
            
    print(HANGMAN_PICS[6])
    print(f"\nGame Over! The correct word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
