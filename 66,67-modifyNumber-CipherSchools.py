# MODIFY NUMBER GUESSING GAME
winning_number=40
guess=1
number=int(input("Enter number between 0 and 100: "))
game_over=False

while not game_over:
    if number==winning_number:
        print(f"You Win,and you guessed this number in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess+=1
            number=int(input("guess again: "))   
        else:
            print("too high")
            guess+=1
            number=int(input("guess again : ")) 



