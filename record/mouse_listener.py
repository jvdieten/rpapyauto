from pynput.mouse import Listener

from model.constants import MOUSE_MOVE_EVENT, MOUSE_CLICK_EVENT, MOUSE_SCROLL_EVENT


class MouseListener:

    def __init__(self, record_file):
        self.record_file = record_file
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

    def on_move(self, x, y):
        self.record_file.write_record('{0},{1},{2}\r\n'.format(MOUSE_MOVE_EVENT, x, y))

    def on_click(self, x, y, button, pressed):
        print('click')
        if pressed:
            self.record_file.write_record('{0},{1},{2},{3}\r\n'.format(MOUSE_CLICK_EVENT, x, y, button))

    def on_scroll(self, x, y, dx, dy):
        self.record_file.write_record('{0},{1},{2},{3},{4}'.format(MOUSE_SCROLL_EVENT,x, y, dx, dy))

    def start_to_listen(self):
        self.listener.start()
        print('Started listening')

    def stop_listening(self):
        self.listener.stop()
        self.record_file.finish()
