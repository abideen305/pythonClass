statement = ""
started = False
while True:
    statement = input(">").lower()
    if statement == "start":
        print("car has started")
    elif statement == "stop":
        print("The car has stopped")
    elif statement == "help":
        print("""
press start to start the car
press stop to stop the car
press help to find help
press any letter to quit     
    """)
    else:
        print("You have quit.")
        break
