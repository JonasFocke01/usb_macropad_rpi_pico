# usb_macropad_rpi_pico
A simple reminder for me how configuring a pi pico with micropython as a keyboard

# Installation

1. Connect the pico in bootsel mode to the computer
2. Download [circuitpython](https://circuitpython.org/board/raspberry_pi_pico/) and drag it onto the pico
3. The pico will unmount and remount as CIRCUITPY
4. Download [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases) and drag the "adafruit_hid" folder onto the pico in `/CIRCUITPY/lib`
5. Install `Thonny`, open it and select `CircuitPython (generic)` in `Run -> Configure interpreter`
6. Open the code from this repo in thonny and click run
