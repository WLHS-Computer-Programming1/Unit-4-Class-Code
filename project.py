import time
import threading
import queue
from time import sleep




def death():
    sleep(1)
    print(youdied)
    sleep(1)
    print(gameover)
    exit()

youdied = r"""

                          .___.__           .___         
 ___.__. ____  __ __    __| _/|__| ____   __| _/         
<   |  |/  _ \|  |  \  / __ | |  |/ __ \ / __ |          
 \___  (  <_> )  |  / / /_/ | |  \  ___// /_/ |          
 / ____|\____/|____/  \____ | |__|\___  >____ |          
 \/                        \/         \/     \/    

 """
gameover = r"""                                                       
   _________    _____   ____     _______  __ ___________ 
  / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \
 / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
 \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
/_____/     \/      \/     \/                   \/       

"""

city = r"""
         /\ \ \ \/_______/     ______/\      \  /\ \/ /\ \/ /\  \_____________
        /\ \ \ \/______ /     /\    /:\\      \ ::\  /::\  /::\ /____  ____ __
       /\ \ \ \/_______/     /:\\  /:\:\\______\::/  \::/  \::///   / /   //
      /\ \ \ \/_______/    _/____\/:\:\:/_____ / / /\ \/ /\ \///___/ /___//___
_____/___ \ \/_______/    /\::::::\\:\:/_____ / \ /::\  /::\ /____  ____  ____
         \ \/_______/    /:\\::::::\\:/_____ /   \\::/  \::///   / /   / /   /
          \/_______/    /:\:\\______\/______/_____\\/ /\ \///___/ /___/ /_____
\          \______/    /:\:\:/_____:/\      \ ___ /  /::\ /____  ____  _/\::::
\\__________\____/    /:\:\:/_____:/:\\      \__ /_______/____/_/___/_ /  \:::
//__________/___/   _/____:/_____:/:\:\\______\ /                     /\  /\::
///\          \/   /\ .----.\___:/:\:\:/_____ // \                   /  \/  \:
///\\          \  /::\\ \_\ \\_:/:\:\:/_____ //:\ \                 /\  /\  /\
//:/\\          \//\::\\ \ \ \\/:\:\:/_____ //:::\ \               /  \/  \/+/
/:/:/\\_________/:\/:::\`----' \\:\:/_____ //o:/\:\ \_____________/\  /\  / /
:/:/://________//\::/\::\_______\\:/_____ ///\_\ \:\/____________/  \/  \/+/\
/:/:///_/_/_/_/:\/::\ \:/__  __ /:/_____ ///\//\\/:/ _____  ____/\  /\  / /  \
:/:///_/_/_/_//\::/\:\///_/ /_//:/______/_/ :~\/::/ /____/ /___/  \/  \/+/\  /
/:///_/_/_/_/:\/::\ \:/__  __ /:/____/\  / \\:\/:/ _____  ____/\  /\  / /  \/
:///_/_/_/_//\::/\:\///_/ /_//:/____/\:\____\\::/ /____/ /___/  \/  \/+/\  /\
///_/_/_/_/:\/::\ \:/__  __ /:/____/\:\/____/\\/____________/\  /\  / /  \/  \
//_/_/_/_//\::/\:\///_/ /_//::::::/\:\/____/  /----/----/--/  \/  \/+/\  /\  /
/_/_/_/_/:\/::\ \:/__  __ /\:::::/\:\/____/ \/____/____/__/\  /\  / /  \/  \/_
_/_/_/_//\::/\:\///_/ /_//\:\::::\:\/____/ \_____________/  \/  \/+/\  /\  /
/_/_/_/:\/::\ \:/__  __ /\:\:\::::\/____/   \ _ _ _ _ _ /\  /\  / /  \/  \/___
_/_/_//\::/\:\///_/ /_//\:\:\:\              \_________/  \/  \/+/\  /\  /   /
/_/_/:\/::\ \:/__  __ /\:\:\:\:\______________\       /\  /\  / /  \/  \/___/_
_/_//\::/\:\///_/ /_//::\:\:\:\/______________/      /  \/  \/+/\  /\  /   /
/_/:\/::\ \:/__  __ /::::\:\:\/______________/\     /\  /\  / /  \/  \/___/___
_//\::/\:\///_/ /_//:\::::\:\/______________/  \   /  \/  \/+/\  /\  /   /   /
/:\/::\ \:/__  __ /:\:\::::\/______________/    \ /\  /\  / /  \/  \/___/___/
/\::/\:\///_/ /_//:\:\:\                         \  \/\\\/+/\  /\  /   /   /+/
\/::\ \:/__  __ /:\:\:\:\_________________________\ ///\\\/  \/  \/___/___/ /_
::/\:\///_/ /_//:\:\:\:\/_________________________////::\\\  /\  /   /   /+/
::\ \:/__  __ /:\:\:\:\/_________________________/:\/____\\\/  \/___/___/ /___
/\:\///_/ /_//:\:\:\:\/_________________________/:::\    /\/\  /   /   /+/   /
\ \:/__  __ /:\:\:\:\/_________________________/:::::\  ///  \/___/___/ /___/_
:\///_/ /_//:\:\:\:\/_________________________/:\:::::\///\  /   /  __________
\:/__  __ /:\:\:\:\/_________________________/:::\:::::\/  \/___/__/\
///_/ /_//:\:\:\:\/_________________________/:\:::\:::::\  /   /  /::\
/__  __ /\::\:\:\/_________________________/_____::\:::::\/___/__/:/\:\
/_/ /_//::\::\:\/_____________________/\/_/_/_/_/\  \           /::\ \:\
_  __ /:\::\:8\/_____________________/\/\   /\_\\/\  \ 8       /:/\:\ \:\
/ /_//\     \|______________________//\\/\::\/__\\/\  \|______/::\ \:\ \:\
 __ /  \  \                        /:\/:\/\_______\/\        /:/\:\ \:\/::\
/_//    8      -8  --  --  --  -- //\::/\\/_/_/_/_/_/ --  --/::\ \:\ \::/\:\
_ /     |\  \   |________________/:\/::\///__/ /__//_______/:/\:\ \:\/::\ \:\
__________\     \               //\::/\:/___  ___ /       /::\ \:\ \::/\:\ \:\
::::::::::\\  \  \             /:\/::\///__/ /__//       /:/\:\ \:\/::\ \:\ \:
"""


#______________________________________________________________________________________________________________________________


character_name = input("what is your name survivor: ")
print(city)
sleep(5)
print("You wake up in a apartment on a couch, you dont know whats going on...")
sleep(2)
print("Your body is aching and bruised...")
sleep(2)
print("you look up at a skylight and see a gray sky, you say…")
sleep(2)
print(f"{character_name} choose either A or B, no other letters. ")
print(" ")

print("A = “Aww shoot, i hate this weather”")
sleep(1)
print("or")
sleep(1)
print("B = stay silent")
print(" ")

answer = input("What do you choose")

#1st choice - you die or survive
if answer.lower() == "a":
    print(f"{character_name}, you chose poorly... ")
    sleep(2)
    print("a zombie behind the couch notices you")
    sleep(1)
    print("The zombie is about to attack you")
    sleep(1)

    def get_input(q):
        user_input = input("Type \"asd\" quickly to get to the bedroom: ")
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
            print(f"You Chose poorly {character_name}")
            death()
    else:
        print(f"You Chose poorly {character_name}")
        death()

#you live
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
    death()

if answer.lower() == "b":
    print("you go to check the computer")
    sleep(2)


print("You figure out you are in st louis, missouri.")
sleep(2)
print("You also find a program connected to cameras outside the house,")
sleep(2)
print("You find the zombie that was waiting outside of the window on the cameras.")
sleep(2)
print("You look for the closest thing but there only appears to be 2 weapons,")
sleep(2)
print("There is a...")
sleep(1)
print(" ")

print("A - a swiss knife -")
print(" ")
sleep(1)
print("or")
print(" ")
sleep(1)
print("B - a pistol -")

answer = input("What do you choose")
print(" ")

if answer.lower() == "a":
    print("you remember your axe throwing skills back in the day and decide to put them to use")
    sleep(2)
    print("You kill the zombie with a hard throw with exceptionally accurate aim.")

#you aim and shoot at the zombie, you kill it but you attract hundreds more, they all storm the house and eat you



#sources
#sleep stuff\/
#https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=Python's%20time%20module%20contains%20many,you%20need%20to%20import%20it.&text=sleep()%20takes%20one%20argument,want%20to%20delay%20your%20code.
