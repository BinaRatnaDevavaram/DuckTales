# Import necessary libraries
import random
import time
from playsound import playsound

# Initialize scores
human_score = 0
computer_score = 0

# Flag to track if at least one round was played
round_played = False

# Define possible outcomes
outcomes = ['rock', 'paper', 'scissors']

icons = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
        }

# Snarky comments

taunts = [
        "👀 Running away already? I barely warmed up.",
        "😏 You scared?",
        "🏃 Fleeing the battlefield, are we?",
        "😆 Rage quit! Classic move.",
        "😴 Bored of losing, huh?"
        ]

win_comments = [
        "You're on fire! 🔥", 
        "Slayed it! ⚔️", 
        "Teach me your ways, sensei. 🧘‍♂️"
        ]

lose_comments = [
        "Oof. That was rough. 😬", 
        "Computer flexed hard! 🤖💪", 
        "Might wanna Google strategy... 📉"
        ]

tie_comments = [
        "A draw? Psychic much? 🔮", 
        "It's a mirror match! 😶", 
        "Mind meld activated! 🧠"]


# Sound effects  

def play_win_sound():
    playsound("sounds/win.wav")

def play_lose_sound():
    playsound("sounds/lose.wav")

def play_tie_sound():
    playsound("sounds/tie.wav")    
    
# Dramatic countdown 

def dramatic_countdown():
    
    for word in ["\nRock... "+str(icons["rock"]), "Paper... "+str(icons["paper"]), "Scissors... "+str(icons["scissors"]), "SHOOT! 💥"]:
        
        print(word)
        
        time.sleep(0.5)

# Start the game
print("\nWelcome to Rock, Paper, Scissors! Let the games begin! 🎮")

# Main game loop
while True:

    print("\nChoose Rock, Paper, Scissors or 'q' to Quit:")
    
    human_choice = input("\n👉 ").lower()

    if human_choice == 'q':
        
        print(f"\n{random.choice(taunts)}")
        print("👋 Fine... Exiting with ahem... style...off you go then! 😏")
        play_lose_sound()
        break

    elif human_choice not in outcomes:
        
        print("\n❌ Invalid choice. That's not how we roll here!😤\n")
        continue
    
    # Set to True only after a valid move
    round_played = True
    
    # Dramatic pause
    dramatic_countdown()

    # Computer's choice
    computer_choice = random.choice(outcomes)
    print(f"\n🤖 Computer chose: {computer_choice} {icons[computer_choice]}")

    # Decide result
    if human_choice == computer_choice:

        print("\n🤝 It's a tie!", random.choice(tie_comments))
        play_tie_sound()

    elif (human_choice == 'rock' and computer_choice == 'scissors') or \
         (human_choice == 'paper' and computer_choice == 'rock') or \
         (human_choice == 'scissors' and computer_choice == 'paper'):

        print("\n✅ You win!", random.choice(win_comments))
        play_win_sound()

        human_score += 1

    else:

        print("\n❌ You lose!", random.choice(lose_comments))
        play_lose_sound()

        computer_score += 1

    
    # Ask if the player wants to play again
    print("\n🔁 Play again? (y/n)")
    
    play_again = input("👉 ").lower()
    
    if play_again != 'y':
    
        print("\n🎭 Game over! Time for final judgment...")
        break

    else:
        # Display current scores
        print(f"\n📊 Current Score - You: {human_score} | Computer: {computer_score}")

# Final results    
if round_played:
    print(f"🏁 Final Score - You: {human_score} | Computer: {computer_score}")

    if human_score > computer_score:
        
        print("🎉 Victory dance time! You're the overall champion! 🏆")
        play_win_sound()
        
    elif human_score < computer_score:

        print("💻 The computer reigns supreme this time. Try again, mortal! ⚡")
        play_lose_sound()
        
    else:

        print("🤷 It's a draw! Truly an epic showdown.")
        play_tie_sound()

# End of the game
print("\n👋 Until next time, warrior! Come back when you're ready for battle! ⚔️ 🛡️")
print("Goodbye!")
