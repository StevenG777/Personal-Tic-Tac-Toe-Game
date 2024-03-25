import random


# 2.1 Create Grid
def createBoard():
  board = []
  for i in range(0, 9):
    board.append("-")
  return board


# 2.2 print the grid
def printBoard(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])


# 2.5 Player Moves
def playerMove(board, coordinate, player_choice):
  print("player Move!")
  player_input = 0
  while True:
    print("Row Number & Column Number with format (RC):")
    print("For Example: 12")
    player_input = int(input().strip())

    if (player_input in coordinate):
      if (board[coordinate[player_input]] != "-"):
        print("The space is occupied, choose another one!")
        continue
      break
    print("Enter a valid move, try again!")

  board[coordinate[player_input]] = player_choice


# 2.6 Computer Moves (Easy)
def computerMoveEasy(board, coordinate, computer_choice, PRINT):
  if PRINT == True:
    print("Computer Random Move!")
  while True:
    random_index = random.randint(0, 8)
    if (board[random_index] == "-"):
      board[random_index] = computer_choice
      break


# 2.6 Computer Moves (Normal)
def computerMoveNormal(board, coordinate, computer_choice):
  print("Computer Smart Move!")
  Easy = True

  # Check Left-Right Consecutive
  left = 0
  right = 1
  # Loop through each row
  for i in range(0, 3):
    # Loop through each two consecutive numbers in a row
    for j in range(0, 2):
      #print("%d == %d" % (left, right))
      # Check if they are equal and make sure they are the right symbol
      if board[left] == board[right] \
      and board[left] != "-" and board[right] != "-" \
      and board[left] != computer_choice and board[right] != computer_choice:
        # i.e. If they are [X X -], Insert "O" such that [X X O] on the right side
        if j == 0 and board[right + 1] == "-":
          board[right + 1] = computer_choice
          # Specify that computerMoveEasy() will not be used
          Easy = not Easy
        # i.e. If they are [- X X], Insert "O" such that [O X X] on the left side
        elif j == 1 and board[left - 1] == "-":
          board[left - 1] = computer_choice
          # Specify that computerMoveEasy() will not be used
          Easy = not Easy
      # Make sure the "left" & "right" index points on the next row
      left += (1 + j)
      right += (1 + j)

  # Check Up-Down Consecutive
  # If Easy is true, This chunk will not be checked
  if Easy == True:
    up = 0
    down = 3
    # Loop through each column
    for i in range(0, 3):
      # Loop through each two consecutive numbers in a column
      for j in range(0, 2):
        #print("%d == %d" % (up, down))
        # Check if they are equal and make sure they are the right symbol
        if board[up] == board[down] \
        and board[up] != "-" and board[down] != "-" \
        and board[up] != computer_choice and board[down] != computer_choice:
          # i.e. If they are [X X -] in vertical, Insert "O" such that [X X O] on the right side
          if j == 0 and board[down + 4] == "-":
            board[down + 3] = computer_choice
            # Specify that computerMoveEasy() will not be used
            Easy = not Easy
          # i.e. If they are [- X X] in vertical , Insert "O" such that [O X X] on the left side
          elif j == 1 and board[up - 4] == "-":
            board[up - 3] = computer_choice
            # Specify that computerMoveEasy() will not be used
            Easy = not Easy
        # Make sure the "up" & "down" index points on the next column
        up += 3
        down += 3
      # Make sure the "up" & "down" index points on the next column
      up -= 5
      down -= 5

  # Check Diagonal From Left To Right Consecutive
  # If Easy is true, This chunk will not be checked
  if Easy == True:
    diag_left = 0
    diag_right = 4
    # Loop through each diagonal entry from top left to bottom right
    for j in range(0, 2):
      #print("%d == %d" % (diag_left, diag_right))
      # Check if they are equal and make sure they are the right symbol
      if board[diag_left] == board[diag_right] \
      and board[diag_left] != "-" and board[diag_right] != "-" \
      and board[diag_left] != computer_choice and board[diag_right] != computer_choice:
        # i.e. If they are [X X -] in diagonal , Insert "O" such that [X X O] on the right side
        if j == 0 and board[diag_right + 4] == "-":
          board[diag_right + 4] = computer_choice
          # Specify that computerMoveEasy() will not be used
          Easy = not Easy
        # i.e. If they are [- X X] in diagonal , Insert "O" such that [O X X] on the right side
        elif j == 1 and board[diag_left - 4] == "-":
          board[diag_left - 4] = computer_choice
          # Specify that computerMoveEasy() will not be used
          Easy = not Easy
      # Make sure the diagnoal index points on the next column
      diag_left += 4
      diag_right += 4

  # Check Diagonal From Right To Left Consecutive
  # If Easy is true, This chunk will not be checked
  if Easy == True:
    diag_right = 2
    diag_left = 4
    # Loop through each diagonal entry from top right to bottom left
    for j in range(0, 2):
      # Check if they are equal and make sure they are the right symbol
      #print("%d == %d" % (diag_left, diag_right))
      if board[diag_right] == board[diag_left] \
      and board[diag_right] != "-" and board[diag_left] != "-" \
      and board[diag_right] != computer_choice and board[diag_left] != computer_choice:
        # i.e. If they are [X X -] in diagonal , Insert "O" such that [X X O] on the right side
        if j == 0 and board[diag_left + 2] == "-":
          board[diag_left + 2] = computer_choice
          # Specify that computerMoveEasy() will not be used
          Easy = not Easy
        # i.e. If they are [- X X] in diagonal , Insert "O" such that [O X X] on the right side
        elif j == 1 and board[diag_right - 2] == "-":
          board[diag_right - 2] = computer_choice
          # Specify that computerMoveEasy() will not be used
          Easy = not Easy
      # Make sure the diagnoal index points on the previous column
      diag_right += 2
      diag_left += 2

  # There is no equal consecutive symbol, use computerMoveEasy()
  if Easy == True:
    computerMoveEasy(board, coordinate, computer_choice, False)


# 2.7 Check for Winning Condition
def winner(board, let):
  return (
    (board[0] == let and board[1] == let and board[2] == let) or  #top R
    (board[3] == let and board[4] == let and board[5] == let) or  #middle R
    (board[6] == let and board[7] == let and board[8] == let) or  #bottom R
    (board[0] == let and board[3] == let and board[6] == let) or  #Left C
    (board[1] == let and board[4] == let and board[7] == let) or  #middle C
    (board[2] == let and board[5] == let and board[8] == let) or  #right C
    (board[0] == let and board[4] == let and board[8] == let) or  #diagonal 1
    (board[6] == let and board[4] == let and board[2] == let))  #diagonal 2


if __name__ == "__main__":
  coordinate = {11: 0, 12: 1, 13: 2, 21: 3, 22: 4, 23: 5, 31: 6, 32: 7, 33: 8}

  player_choice = ""
  computer_choice = "X"
  turn = ""
  setting = ""
  again = True

  # Game Started
  while again == True:
    occupied = 0
    win = False
    board = createBoard()
    while True:
      # 2.10 Choose Easy/Normal Setting
      print("Please Select the Difficulty: (Easy/Normal)")
      setting = input()
      if (setting.upper() == "EASY" or setting.upper() == "NORMAL"):
        break
      print("Please enter valid setting, try again!")

    # 2.3 Player Chooses Symbol and Setting
    while True:
      print("Please choose X or O as player")
      user_input = input().strip()
      if user_input == "X" or user_input == "x" or user_input == "O" or user_input == "o":
        player_choice = user_input.upper()
        if (player_choice == computer_choice):
          computer_choice = "O"
        break
      print("Please don't choose invalid choice!")
    print("player choice: %s" % player_choice)
    print("computer choice: %s" % computer_choice)

    # 2.4 Player and Computer Determine First Turn
    if player_choice == "X":
      turn = "PLAYER"
    else:
      turn = "COMPUTER"
    print("%s has first turn!" % turn)
    print()

    # 2.7 While loop checks for tying condition
    while (occupied < 9):
      current_let = ""
      if (turn == "PLAYER"):
        playerMove(board, coordinate, player_choice)
        occupied = occupied + 1
        turn = turn.replace("PLAYER", "COMPUTER")
        current_let = current_let.replace(current_let, player_choice)
      else:
        if (setting.upper() == "EASY"):
          computerMoveEasy(board, coordinate, computer_choice, True)
        else:
          computerMoveNormal(board, coordinate, computer_choice)
        occupied = occupied + 1
        turn = turn.replace("COMPUTER", "PLAYER")
        current_let = current_let.replace(current_let, computer_choice)

      # 2.2 Print Grid
      printBoard(board)
      print()

      # 2.7 Check for Winning Condition
      if winner(board, current_let) == True:
        win_role = ""
        if turn == "PLAYER":
          win_role = "COMPUTER"
          win = not win
        else:
          win_role = "PLAYER"
          win = not win
        print("%s WINS!!!" % win_role)
        break

    # 2.7 Check for Tying Condition
    if occupied == 9 and win == False:
      print("COMPUTER AND PLAYER ARE IN TIE!!!")

    # 2.8 End of the Match Message
    print("GAME OVER!!!")
    print()

    # 2.9 Play Again?
    while True:
      print("Play again? (Y/N)")
      answer = input()
      if answer.upper() == "Y" or answer.upper() == "YES":
        again = True
        break
      elif answer.upper() == "N" or answer.upper() == "NO":
        again = False
        print("Thank You For Playing!")
        break
      else:
        print("Reponse is invalid! Try again!")
