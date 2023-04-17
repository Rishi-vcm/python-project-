import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why couldn't the bicycle find its way home? It lost its bearings!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What's a skeleton's least favorite room in the house? The living room!"
]

# Function to get a random joke from the list
def get_joke():
    return random.choice(jokes)

# Main loop
while True:
    # Display menu options
    print("Welcome to Joke Generator!")
    print("1. Get a joke")
    print("2. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Get and display a random joke
        joke = get_joke()
        print("Joke: ", joke)
    elif choice == "2":
        # Exit the program
        print("Thank you for using Joke Generator!")
        break
    else:
        # Invalid input
        print("Invalid choice. Please try again.")
