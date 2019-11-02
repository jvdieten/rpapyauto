from record.mouse_listener import MouseListener
from record.record_file import Recordfile


class Recorder:

    def start(self):
        record_file = Recordfile()
        self.mouse_listener = MouseListener(record_file)
        print('start record')
        self.mouse_listener.start_to_listen()

    def stop(self):
        self.mouse_listener.stop_listening()
