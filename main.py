import random
import time

import pyautogui
from loguru import logger
from pynput.keyboard import Key

from click_button import click_button_once
from listener.keyboard import listener as keyboard_listener

SLEEP_SEC = 0.27
STOP_KEY = Key.esc


def alert_scripts_starting():
    pyautogui.alert('Scripts now starting!')


def run_scripts():
    logger.info("Starting keyboard listener")
    keyboard_listener.start()

    logger.info("Starting scripts")
    alert_scripts_starting()

    while keyboard_listener.get_last_pressed_key() != STOP_KEY:
        click_button_once('1')
        time.sleep(random.uniform(0, SLEEP_SEC))

    logger.info("Finished running scripts")


if __name__ == '__main__':
    run_scripts()
