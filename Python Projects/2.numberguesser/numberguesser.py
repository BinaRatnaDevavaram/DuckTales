#Import necessary libraries
import random
import webbrowser
import os
import winsound


# Function to play sound in the background
def play_sound(audio_path):
                
    winsound.PlaySound(audio_path, winsound.SND_FILENAME)
    
    
#Angry GIF for invalid user inputs
def angry_gif():
    
    #Angry meme audio file path
    audio_path = os.path.abspath("angry.wav")

    # Open angry meme GIF from the web
    webbrowser.open("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTZmbmR1bjVzYjZobnNkZHFyMzE1bTR2bm9ld255cHBmaGkzcDBzYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9u3TZfpmeDLkD6/giphy.gif")

    # Play sound
    play_sound(audio_path)    
        

    
#Party GIF for final win
def party_gif():
    
    # Party audio file path
    audio_path = os.path.abspath("party.wav")

    # Open celebration GIF from the web
    webbrowser.open("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG9mY3c4cWQ2NTdyOGRjcXdqMmJ5MWQ5dWNiM243aGtxem51OTF3aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oXipRwi4QSemGw9D4B/giphy.gif")

    # Play sound
    play_sound(audio_path)



#Ask the user for the maximum number they want to guess
top_of_range = input("\nEnter a max limit number from 5 to 10, no words: ")

# Check if the input is a digit
if top_of_range.isdigit():
 
    # Convert the input to an integer
    top_of_range = int(top_of_range)
 
    # Quit if the input is 0 or negative    
    if top_of_range <= 0:
        angry_gif()
        print("\nBruh.. Enter a number > 0 next time.")
        quit()
        
    elif top_of_range < 5 or top_of_range > 10:
        angry_gif()
        print("\nWake up sleepyhead! Enter a number between 5 and 10 next time.")
        quit()

else:
    angry_gif()
    print("\nHow egregious!! Enter a positive number next time.")
    quit()

# Generate a random number between 1 and top_of_range 
random_number = random.randint(1,top_of_range) 

# Initialize the number of guesses
number_of_guesses = 0

# While loop to allow the user to guess the number
while True:
    
    # Increment the number of guesses
    number_of_guesses += 1
    
    # Ask the user to guess the number
    user_guess = input("\nGuess the number: ")
    
    # Check if the input is a digit
    if user_guess.isdigit():
        
        user_guess = int(user_guess)
        
        if user_guess < 1 or user_guess > top_of_range:
            print(f"\nC'mon! Enter a number between 1 and {top_of_range}.")
            continue    
    else:
        print("\nHmpf! Enter a valid number.")
        continue
    
    # Check if the guess is correct
    if user_guess == random_number:
        party_gif()
        print("\nCongratulations! You guessed the number!")
        break
    
    elif user_guess < random_number:
        print("\nToo low! Try again.")
    
    else:
        print("\nToo high! Try again.")
        
print(f"\nYAY!!! You guessed the number in {number_of_guesses} tries!")

print("\nThanks for playing the Number Guesser Game!")
# End of the game