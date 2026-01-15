import os
import json
import random

Difficulty = {
    "1" : {"easy": 10},
    "2" : {"medium": 5},
    "3" : {"hard": 3}
}
def get_random_number():
    return random.randint(1, 100)
def load_scores():
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as file:
            return json.load(file)
    return {}
def save_scores(scores):
    with open("scores.json", "w") as file:
        json.dump(scores, file)

def update_score(player_name, difficulty, attempts):
    scores = load_scores()

    # Ensure root structure exists
    if "players" not in scores:
        scores["players"] = {}

    # Ensure player exists
    if player_name not in scores["players"]:
        scores["players"][player_name] = {
            "easy": {"games_played": 0, "best_attempts": None, "history": []},
            "medium": {"games_played": 0, "best_attempts": None, "history": []},
            "hard": {"games_played": 0, "best_attempts": None, "history": []}
        }

    player_data = scores["players"][player_name][difficulty]

    # Update statistics
    player_data["games_played"] += 1
    player_data["history"].append(attempts)

    # Update best attempts
    if player_data["best_attempts"] is None or attempts < player_data["best_attempts"]:
        player_data["best_attempts"] = attempts

    save_scores(scores)


def display_scores():
    scores = load_scores()

    if not scores or "players" not in scores or not scores["players"]:
        print("\nNo scores available yet.\n")
        return

    print("\n--- Scoreboard ---")

    for player, difficulties in scores["players"].items():
        print(f"\nPlayer: {player}")
        for difficulty, details in difficulties.items():
            games = details["games_played"]
            best = details["best_attempts"]
            history = details["history"]

            best_display = best if best is not None else "N/A"

            print(
                f"  Difficulty: {difficulty.capitalize()} | "
                f"Games Played: {games} | "
                f"Best Attempts: {best_display} | "
                f"History: {history}"
            )

    print("------------------\n")

def play_game(chances):
    number_to_guess = get_random_number()
    attempts = 0

    while attempts < chances:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{chances}. Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            return attempts

    print(f"Sorry, you've used all your chances. The correct number was {number_to_guess}.")
    return None

def main():
    print(
        "Welcome to the Number Guessing Game!\n"
        "I'm thinking of a number between 1 and 100.\n"
    )

    player_name = input("Please enter your name: ").strip()

    # Clean difficulty mapping
    difficulty_map = {
        "1": ("easy", 10),
        "2": ("medium", 5),
        "3": ("hard", 3)
    }

    while True:
        display_scores()

        print("Select an option:")
        print("1. Play Game")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            print("\nSelect Difficulty Level:")
            print("1. Easy (10 chances)")
            print("2. Medium (5 chances)")
            print("3. Hard (3 chances)")

            difficulty_choice = input("Enter your choice (1, 2, or 3): ").strip()

            if difficulty_choice not in difficulty_map:
                print("Invalid difficulty choice.\n")
                continue

            difficulty_name, chances = difficulty_map[difficulty_choice]

            print(f"\nYou selected {difficulty_name.capitalize()} difficulty.")
            attempts = play_game(chances)

            if attempts is not None:
                update_score(player_name, difficulty_name, attempts)

        elif choice == "2":
            print("Thank you for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.\n")


if __name__ == "__main__":
    main()




