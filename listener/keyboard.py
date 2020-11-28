from loguru import logger
from pynput import keyboard

STOP_SCRIPTS = False


class StatefulListener(keyboard.Listener):

    def __init__(self, *args, **kwargs):
        self.last_pressed_key = None
        super(StatefulListener, self).__init__(*args, **kwargs)

    def get_last_pressed_key(self):
        return self.last_pressed_key


def on_press(key):
    try:
        logger.debug(f'alphanumeric key {key.char} pressed')
    except AttributeError:
        logger.error(f'special key {key} pressed')
    listener.last_pressed_key = key


def on_release(key):
    logger.debug(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = StatefulListener(on_press=on_press, on_release=on_release)
