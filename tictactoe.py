tictac = [" " for x in range(9)]
def board():
    row1=f"| {tictac[0]} | {tictac[1]} | {tictac[2]} |"
    row2=f"| {tictac[3]} | {tictac[4]} | {tictac[5]} |"
    row3=f"| {tictac[6]} | {tictac[7]} | {tictac[8]} |"
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def move(chara):
        try:
            if chara=="X":
                number=1
            elif chara=="O":
                number=2
            print("Options:")
            print("|1|2|3|\n|4|5|6|\n|7|8|9|")
            print(f"Your turn player {number}")
            choice=int(input("Enter your move (1-9):"))
            if tictac[choice-1]==" ":
                tictac[choice-1]=chara
            else:
                print()
                print("That space is already occupied!")
                move(chara)
        except (IndexError,ValueError):
            print("Invalid input. Please enter a value between 1 and 9")
            move(chara)

def win(icon):
    if (tictac[0]==icon and tictac[1]==icon and tictac[2]==icon) or (tictac[3]==icon and tictac[4]==icon and tictac[5]==icon) or (tictac[6]==icon and tictac[7]==icon and tictac[8]==icon) or (tictac[0]==icon and tictac[3]==icon and tictac[6]==icon) or (tictac[1]==icon and tictac[4]==icon and tictac[7]==icon) or (tictac[2]==icon and tictac[5]==icon and tictac[8]==icon) or (tictac[0]==icon and tictac[4]==icon and tictac[8]==icon) or (tictac[2]==icon and tictac[4]==icon and tictac[6]==icon):
        return True
    else:
        return False
    
def draw():
    if " " not in tictac:
        return True
    else:
        return False
    
while True:
    board()
    move("X")
    board()
    if win("X"):
        print("Player 1 wins Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break
    move("O")
    if win("O"):
        board()
        print("player 2 wins Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break