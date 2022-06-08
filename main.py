from random import choice

game = ["R", "P", "S"]
opt = {"R":"Rock", "P":"Paper", "S":"Scissors"}

play = True

while play:

   player_opt = input("Enter option, between R, P, or S: ")

   while play:

      if player_opt == game[0] or player_opt == game[1] or player_opt == game[2]:
         play = False
      else:
         player_opt = input("Invalid option! Please, choose between R, P, or S: ")

   computer_opt = choice(game)

   print("Player", "(" + opt[player_opt] + ")", ":", "CPU", "(" + opt[computer_opt] + ")")

   p, c = player_opt, computer_opt

   if p == "R" and c == "S" or p == "S" and c == "P" or p == "P" and c == "R":
      print("Game over, Player wins!")
   elif player_opt == computer_opt:
      print("Snap! That's a tie! Don't frown, play again.")
      play = True
   else:
      print("Game over, CPU wins!")

