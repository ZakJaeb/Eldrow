# eldrow.py

""" guess = input("Guess a word: ").upper()
if guess == "SNAKE":
    print("Correct")
else:
    print("Wrong") """

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == "SNAKE":
        print("Correct")
        break

    print("wrong")