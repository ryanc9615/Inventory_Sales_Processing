import random
import time

total_time = 60 * 3 # 3 mintues
start_time = time.time()
score = 0
puzzle_count = 0


print("Welcome to the Math Puzzle Game!")
print("You have 3 minutes to solve as many puzzles as you can.")
print("Points are rewarded for correct answers and deducted for incorrect ones.")
print("Select the difficulty level:")
print("1. Easy (Addition/Subtraction)")
print("2. Medium (Multiplication/Division)")
print("3. Hard (Patterns and Mixed operations")

difficulty = input("Enter the difficulty level (1/2/3): ").strip()

if difficulty == "1":
    level = "easy"
elif difficulty == "2":
    level = "medium"
elif difficulty == "3":
    level = "hard"
else:
    print("Invalid choice, defaulting to easy mode.")
    level = "easy"
