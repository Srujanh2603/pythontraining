import random
def generate(l,h):
    return random.randint(l,h)
def check_guess(secret,guess):
    if guess < secret:
        return "too low"
    elif guess > secret:
        return "too high"
    else:
        return "correct"

def main():
    l=1
    h=100
    secretno=generate(l,h)
    print("welcome to number guessing gaming!")
    print(f'Guess the number between {l} and {h}')
    guesses=0
    while True:
        guess=int(input("Enter your guess: "))
        result=check_guess(secretno,guess)
        print(result)
        guesses=guesses+1
        if result == "correct":
            print(f"You guessed it right!, You guessed the number in {guesses} guesses")
            break
        else:
            print(result)

if __name__ == '__main__':
    main()