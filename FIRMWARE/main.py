# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.extensions.append(MediaKeys())

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10]
encoder_handler.pins = ((board.D0, board.D1, None))

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),), 
]


# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MACRO("hi"), KC.Macro(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), KC.MACRO("http://www.youareanidiot.cc"),Tap(KC.ENTER)), KC.MACRO(Tap(KC.ESC), Tap(KC.R), Tap(KC.ENTER)), KC.MACRO("dweeb")]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
