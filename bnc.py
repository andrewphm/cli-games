from random import randint




def play_game():
    roles = ["Bear", "Ninja", "Cowboy"]
    player = False
    score = 0

    while player == False:
        player = input("Bear, Ninja, or Cowboy? > ")
        computer = roles[randint(0,2)]

        
        score = check_winner(player, computer, score)

        print(f"Your score is {score}")
        play_again = input("Would you like to play again? (yes/no) > ")    
        if play_again == 'yes':
            player = False





def check_winner(player, computer, score):
    if computer == player:
        print("DRAW!")
        return score + 0
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", player, "is shot by", computer)
            return score - 1
        else:
            print("You win!", player, "defeats", computer)
            return score + 1
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
            return score + 1
        else:
            print("You lose!", player, "is eaten by", computer)
            return score - 1
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeated by", computer)
            return score - 1
        else:
            print("You win!", player, "eats", computer)
            return score + 1


play_game()
