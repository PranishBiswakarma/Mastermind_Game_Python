import random 

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    while True:
        guess = input("Guess (e.g. R G B Y): ").upper().split()
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        invalid = False
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                invalid = True
        if invalid:
            continue  # ask again for a valid guess
        return guess

def check_code(guess, real_code):
    correct_pos = 0
    incorrect_pos = 0
    
    real_code_copy = real_code[:]
    guess_copy = guess[:]

    # Check for correct position and color
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            real_code_copy[i] = None
            guess_copy[i] = None

    # Check for correct color, wrong position
    for i in range(CODE_LENGTH):
        if guess_copy[i] is not None and guess_copy[i] in real_code_copy:
            incorrect_pos += 1
            real_code_copy[real_code_copy.index(guess_copy[i])] = None

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind. You have {TRIES} tries to guess the combo.")
    print("The valid colors are:", *COLORS)

    code = generate_code()
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"Congratulations! You guessed the code in {attempt} tries!")
            break

        print(f"Correct Position: {correct_pos} | Incorrect Position: {incorrect_pos}")

    else:
        print("You ran out of luck! The combo was:", *code)

if __name__ == "__main__":
    game()
