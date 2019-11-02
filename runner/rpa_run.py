from model.constants import MOUSE_MOVE_EVENT, MOUSE_CLICK_EVENT
from runner.run_loader import Runloader

import pyautogui

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True


class RPArun:

    def __init__(self, item):
        self.runLoader = Runloader(item)

    def run(self):
        print('IN RUN..')
        self.runLoader.load_items()
        for item in self.runLoader.actionlist:
            action = item.split(',')
            print(action)
            if action[0] == MOUSE_MOVE_EVENT:
                pyautogui.move(float(action[1]), float(action[2]))
            elif action[0] == MOUSE_CLICK_EVENT:
                pyautogui.click(float(action[1]), float(action[2]))
