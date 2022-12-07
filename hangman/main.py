import re
import random

# Getting the answer
pool_file = open("hangman/hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

answer = answer.upper()

# Game setup.
num_of_incorrect_guesses = 5

answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# Game logic.
current_incorrect_guesses = 0

