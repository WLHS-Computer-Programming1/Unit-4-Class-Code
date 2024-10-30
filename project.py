import time
import threading
import queue
from time import sleep


character_name = input("what is your name survivor: ")

youdied = r"""

                          .___.__           .___         
 ___.__. ____  __ __    __| _/|__| ____   __| _/         
<   |  |/  _ \|  |  \  / __ | |  |/ __ \ / __ |          
 \___  (  <_> )  |  / / /_/ | |  \  ___// /_/ |          
 / ____|\____/|____/  \____ | |__|\___  >____ |          
 \/                        \/         \/     \/          
                                                         
   _________    _____   ____     _______  __ ___________ 
  / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \
 / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
 \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
/_____/     \/      \/     \/                   \/       

"""


sleep(1)
print("You wake up in a house on a couch, you dont know whats going on...")
sleep(2)
print("Your body is aching and bruised...")
sleep(2)
print("you look up in the skylight and see a gray sky, you say…")
sleep(2)
print(f"{character_name} choose either A or B, no other letters. ")
print(" ")

print("A = “Aww shoot, i hate this weather”")
print("B = stay silent")
print(" ")

answer = input("What do you choose")


#1st choice
if answer.lower() == "a":
    print(f"{character_name}, you chose poorly... ")
    sleep(2)
    print("a zombie behind the couch notices you")
    sleep(1)
    print("The zombie is about to attack you")
    sleep(1)

    def get_input(q):
        user_input = input("Type 'asd' to get to the bedroom: ")
        q.put(user_input)  # Put the input into the queue


    input_queue = queue.Queue()

    # Start the input thread
    input_thread = threading.Thread(target=get_input, args=(input_queue,))
    input_thread.start()

    # Wait for 5 seconds, providing countdown
    for i in range(5, 0, -1):
        print(f"{i} seconds remaining")
        time.sleep(1)

    # Check if the input thread is still alive
    if input_thread.is_alive():
        print("Time's up! Stopped.")
        # Attempt to terminate the input thread
        input_thread.join(timeout=0)  # This will ensure the main thread continues without waiting

    # Check if we got any input
    user_input = None  # Initialize user_input
    if not input_queue.empty():
        user_input = input_queue.get()  # Retrieve input from the queue
        print(f"You entered: {user_input}")
    else:
        print("No input received.")

    # Handle user input
    if user_input is not None:
        if user_input == "asd":
            print("You escaped! you run to the nearest door you can find.")
            sleep(2)
          
        else:
            print("You died.")
    else:
        print("You died, no input received.")


elif answer.lower() == "b":
    print("nothing happens")
    sleep(2)
    print("you look around to see the zombie behind the couch that you are sleeping on")
    sleep(2)
    print("you move quietly to the bedroom")
    sleep(2)


print(" ")
print("You are in the bedroom, you see a computer and you see a window, ")
sleep(2)
print("Do you…")
print(" ")
sleep(2)

print("A  - Look out the window, see whats going on,")
sleep(1)
print("or...")
sleep(1)
print("B - Check the computer,")
sleep(2)
print("")

answer = input("What do you choose - A or B")


if answer.lower() == "a":
    print(f"{character_name}, you chose poorly... ")
    sleep(2)
    print("you look out and a zombie breaks through the window and bites off your face")
    sleep(1)
    print(youdied)

#elif answer.lower() == "b":
#- you figure out you are in Louisiana, Texas.
#You also find a program connected to cameras outside the house,
#you find the zombie that was waiting outside of the window on the cameras.
#You look for the closest thing but there appears to be 2 weapons,



#sources
#sleep stuff\/
#https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=Python's%20time%20module%20contains%20many,you%20need%20to%20import%20it.&text=sleep()%20takes%20one%20argument,want%20to%20delay%20your%20code.
