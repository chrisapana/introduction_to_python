# while loop

command = ""
started = False
stopped = False


while True:
 command = input("> ").lower()
 if command == "start":
  if started:
   print("You have already started")
  else:
   started = True
   print("You just got started...haha")
 elif command == "stop":
  if not started:
   print("You've exitted")
  else:
   started = False
   print("Start to begin")
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

