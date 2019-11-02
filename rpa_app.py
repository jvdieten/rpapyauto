import remi.gui as gui
from remi import start, App
import glob

from record.recorder import Recorder
from runner.rpa_run import RPArun


class RpaApp(App):

    def main(self, name='world'):
        self.record = Recorder()

        # margin 0px auto allows to center the app to the screen
        self.wid = gui.VBox(width='100%', height='100%')
        items = glob.glob("tmp/*.txt")

        self.listView = gui.ListView.new_from_list(items, width=200, height=100, margin='10px 50px')
        self.listView.onselection.do(self.list_view_on_selected)

        recordbtn = gui.Button('Record', width=200, height=30)
        recordbtn.style['margin'] = '10px 50px'
        recordbtn.style['background-color'] = 'green'
        recordbtn.onclick.do(self.on_recordbtn_pressed)

        stopRecordbtn = gui.Button('Stop recording', width=200, height=30)
        stopRecordbtn.style['margin'] = '10px 50px'
        stopRecordbtn.style['background-color'] = 'orange'
        stopRecordbtn.onclick.do(self.on_stoprecordbtn_pressed)

        self.executebtn = gui.Button('Execute', width=200, height=30)
        self.executebtn.style['margin'] = '10px 50px'
        self.executebtn.style['background-color'] = 'blue'

        self.executebtn.onclick.do(self.on_executebtn_pressed)

        self.lbl = gui.Label('', width=200, height=30, margin='10px 50px')

        self.wid.append(recordbtn)
        self.wid.append(stopRecordbtn)
        self.wid.append(self.listView)
        self.wid.append(self.lbl)

        return self.wid

    def on_recordbtn_pressed(self, _):
        print("Start recording.")
        self.record.start()

    def on_stoprecordbtn_pressed(self, _):
        print("Stop recording.")
        self.record.stop()
        self.listView.empty()
        items = glob.glob("tmp/*.txt")
        self.listView.append(items)

    def on_executebtn_pressed(self, _):
        print("Start execution.")
        rpa = RPArun(self.activeItem)
        rpa.run()

    def list_view_on_selected(self, widget, selected_item_key):
        self.activeItem = self.listView.children[selected_item_key].get_text()
        self.lbl.set_text('Selected for run: ' + self.activeItem)
        self.wid.append(self.executebtn)


def on_close(self):
    super(RpaApp, self).on_close()


if __name__ == "__main__":
    start(RpaApp, standalone=True)
