import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import digitalio
import board

# Define the buttons and their corresponding key codes
buttons = {
    0: Keycode.A,  # 'a'
    1: Keycode.B,  # 'b'
    2: 0x06,  # 'c'
}

# Initialize the buttons
button_pins = [digitalio.DigitalInOut(getattr(board, f'GP{key}')) for key in buttons.keys()]
for button in button_pins:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    
# Initialize the keyboard HID device
kbd = Keyboard(usb_hid.devices)

def send_key(key_code):
    # Press and release the 'A' key
    kbd.press(key_code)
    time.sleep(0.1)
    kbd.release(key_code)

while True:
    for i, button in enumerate(button_pins):
        if not button.value:  # Button pressed
            send_key(buttons[i])
            time.sleep(0.1)  # Debounce delay
