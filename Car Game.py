# Car different states simulations
# Building the engine stats start - stop - help - quit
is_started = False
while True:
    command = input(">").lower()
    if command == "start":
        if is_started:
            print("Car is already started!")
        else:
            print("Car started...Ready to go!")
            is_started = True
    elif command == "stop":
        if not is_started:
            print("Car is already stopped!")
        else:
            print("Car stopped.")
            is_started = False
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")

