import time
import threading
import queue
from time import sleep

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
        print("You escaped!")
    else:
        print("You died.")
else:
    print("You died, no input received.")

# Terminate the program
exit()

