# while loop

command = ""

while True:
 command = input("> ").lower()
 if command == "start":
  print("You just got started...haha")
 elif command == "stop":
  print("You've gotten to your destination")
 elif command == "help":
  print("""
start -- to start the game
stop -- to end the game
quit -- to quit
     """)
 elif command == "quit":
  break
 else:
  print("Oops, you need the instructions! type help😁")


# while command.lower() != "quit":
#  command = input("> ")
#  if command.lower() == "start":
#   print("You just got started...haha")
#  elif command.lower() == "stop":
#   print("You've gotten to your destination")
#  elif command == "help":
#   print("""
# start -- to start the game
# stop -- to end the game
# quit -- to quit
#      """)
#  else:
#   print("Oops, you need the instructions! type help😁")
