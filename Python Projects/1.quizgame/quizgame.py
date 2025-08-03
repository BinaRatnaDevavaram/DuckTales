# Import necessary libraries
import random
from playsound import playsound


# Greet the user
print("\nWelcome to this Quiz on Countries and Capitals!")
initiate = input("\nDo you want to play? Type yes/no: ")

# Check if the user wants to play

# If they don't type yes, exit the game
if initiate.strip().lower() not in ["yes", "y"]: 
    print("\n😒 Boo-hoo! That was... impressive. Not.")
    print("Cool cool cool… no doubt no doubt. You’ll totally come back. Eventually. Probably. Maybe. 👀")
    playsound('boo.mp3')  # Play sound for exit
    quit()
    
# If they type yes, continue with the game
else:
    
    print("\nGreat! Let's get started.")
    
    print("\nYou will be asked 5 questions.\nLet's see how many you can answer correctly!")
    
    playsound('start.mp3')  # Play sound to start the game
    
    score = 0
    
    # Store all 20 Q & A in a list of dictionaries
    questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is the capital of Japan?", "answer": "tokyo"},
    {"question": "What is the capital of Canada?", "answer": "ottawa"},
    {"question": "What is the capital of Australia?", "answer": "canberra"},
    {"question": "What is the capital of Brazil?", "answer": "brasilia"},
    {"question": "What is the capital of Germany?", "answer": "berlin"},
    {"question": "What is the capital of Italy?", "answer": "rome"},
    {"question": "What is the capital of Egypt?", "answer": "cairo"},
    {"question": "What is the capital of India?", "answer": "new delhi"},
    {"question": "What is the capital of China?", "answer": "beijing"},
    {"question": "What is the capital of South Korea?", "answer": "seoul"},
    {"question": "What is the capital of Russia?", "answer": "moscow"},
    {"question": "What is the capital of Kenya?", "answer": "nairobi"},
    {"question": "What is the capital of Argentina?", "answer": "buenos aires"},
    {"question": "What is the capital of Mexico?", "answer": "mexico city"},
    {"question": "What is the capital of Spain?", "answer": "madrid"},
    {"question": "What is the capital of Portugal?", "answer": "lisbon"},
    {"question": "What is the capital of Netherlands?", "answer": "amsterdam"},
    {"question": "What is the capital of Thailand?", "answer": "bangkok"},
    {"question": "What is the capital of Nigeria?", "answer": "abuja"}
    ]

    # Randomly pick 5 questions
    selected_questions = random.sample(questions, 5)

    # Ask the questions by looping through selected ones
    for q in selected_questions:
        
        answer = input(f"\n{q['question']} ")
        
        if answer.strip().lower() == q['answer']:
            print("\nCorrect!")
            playsound('correct.mp3')  # Play sound for correct answer
            score += 1
            
        else:
            print(f"\nIncorrect! The answer is {q['answer'].title()}.")
            playsound('wrong.mp3')  # Play sound for incorrect answer
    
    # Display the final score 
    print(f"\n🎉 You nailed {score} out of 5 - that's a {(score / 5) * 100}% accuracy!")
    print("🙌 Thanks for playing, you magnificent brainiac!!")
    print("✨ Stay curious and keep flexing those learning muscles! 🧠\n")
    playsound('cheer.mp3')  # Play sound for end of game
